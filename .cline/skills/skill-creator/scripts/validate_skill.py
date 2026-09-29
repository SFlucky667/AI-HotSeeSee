#!/usr/bin/env python3
"""Validate the structure of a Cline Agent Skill directory.

Usage:
    python validate_skill.py <skill_dir>

Checks that:
  - SKILL.md exists at the root of the skill directory
  - SKILL.md starts with valid YAML front-matter containing 'name' and 'description'
  - front-matter 'name' matches the directory name
  - referenced scripts exist and are syntactically valid Python
  - referenced references/ files exist
Exit code 0 on success, 1 on any failure.
"""
import os
import re
import sys
import py_compile


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python validate_skill.py <skill_dir>")
        return 2

    skill_dir = os.path.abspath(sys.argv[1])
    errors = []

    if not os.path.isdir(skill_dir):
        print(f"[ERROR] Not a directory: {skill_dir}")
        return 1

    dir_name = os.path.basename(skill_dir)
    skill_md = os.path.join(skill_dir, "SKILL.md")

    # 1. SKILL.md must exist
    if not os.path.isfile(skill_md):
        errors.append(f"Missing SKILL.md in {skill_dir}")
    else:
        with open(skill_md, "r", encoding="utf-8") as f:
            text = f.read()

        # 2. Front-matter must be present at the very top
        if not text.startswith("---"):
            errors.append("SKILL.md must start with YAML front-matter delimited by '---'")
        else:
            match = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
            if not match:
                errors.append("SKILL.md front-matter is not terminated correctly (--- ... ---)")
            else:
                fm = match.group(1)
                name = re.search(r"^name:\s*(.+)$", fm, re.M)
                desc = re.search(r"^description:\s*.+$", fm, re.M)
                if not name:
                    errors.append("Front-matter missing required key: name")
                elif name.group(1).strip() != dir_name:
                    errors.append(f"Front-matter name '{name.group(1).strip()}' != directory name '{dir_name}'")
                if not desc:
                    errors.append("Front-matter missing required key: description")

        # 3. Check referenced local files exist
        for ref in re.findall(r"\]\(([^)]+)\)", text):
            target = ref.split("#")[0]
            if target.startswith("http") or target.startswith("#"):
                continue
            full = os.path.normpath(os.path.join(skill_dir, target))
            if not os.path.exists(full):
                errors.append(f"Referenced file does not exist: {ref}")

        # 4. Check referenced scripts are valid Python
        for ref in re.findall(r"`([^`]*?\.py)`", text):
            full = os.path.normpath(os.path.join(skill_dir, ref))
            if os.path.isfile(full):
                try:
                    py_compile.compile(full, doraise=True)
                except py_compile.PyCompileError as e:
                    errors.append(f"Python syntax error in {ref}: {e}")

    if errors:
        print(f"[FAIL] {len(errors)} problem(s) found:")
        for e in errors:
            print("  - " + e)
        return 1

    print(f"[OK] Skill '{dir_name}' structure is valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
