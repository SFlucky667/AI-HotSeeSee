---
name: skill-creator
description: >
  Create and refine reusable agent skills for this project. Use when the user asks to build a new skill,
  "创建新技能", "新建一个技能", "帮我把 XX 做成技能", add a SKILL.md, scaffold a skill directory,
  improve an existing skill, or package recurring instructions as a callable skill.
---

# Skill Creator — 技能创建与完善

引导如何在本项目（Cline Agent Skills）中**设计、编写、组织并验证**一个可复用的技能，
使一个重复性工作流程被封装成可由 AI 直接调用的技能。

## 技能的基本概念

一个 Cline 技能是一个**目录**，根目录下必须包含 `SKILL.md`。目录结构示例：

```
skills/<skill-name>/
├── SKILL.md              # 必需：技能定义与使用说明（front-matter + 正文）
├── references/           # 可选：详细背景资料、规范、判定标准
├── scripts/              # 可选：技能依赖的 Python/Shell 脚本
├── assets/               # 可选：模板、样例、静态资源
└── data/                 # 可选：技能运行时读取的数据/目录
```

## 创建新技能的分步流程

### 第 1 步：明确技能目标与触发场景
- 明确这个技能解决什么问题、在什么场景被调用。
- 列出用户可能用来触发该技能的**中文 + 英文**说法，写入 `description`。

### 第 2 步：选择技能名称
- 全小写、用连字符 `-` 连接单词（如 `hot-monitor`）。
- 名称要简洁且在项目中唯一。

### 第 3 步：编写 `SKILL.md`

`SKILL.md` 严格分为两部分：**front-matter（YAML 元数据）** + **Markdown 正文**。

**front-matter 模板：**
```yaml
---
name: <skill-name>
description: >
  一到两句话说明技能用途；然后列出触发它被调用的常见说法（中英皆可），用逗号分隔。
---
```

**正文应包含（按此顺序组织）：**
1. **标题与一句话说明**：`# 技能名 — 作用概述`
2. **前置条件/Quick Start**：环境变量、依赖安装命令。
3. **核心工作流**：分步骤的、明确的操作指令（用户/模型该怎么一步步执行）。
4. **脚本参考表**：列出 `scripts/` 下每个脚本的用法、参数、输入输出。
5. **错误处理**：脚本失败 / 边界情况如何处理。
6. **进阶模式**：关键词扩展、批量、特殊 Flag 等。
7. **参考文件链接**：指向 `references/` 下可深入阅读的文档。

### 第 4 步：组织子目录
- 需要外部资料 → 放 `references/*.md`，并在 SKILL.md 正文中链接。
- 需要可执行逻辑 → 放 `scripts/*.{py,sh}`，提供 `--help`、清晰的参数和 stdout/JSON 输出约定。
- 提供模板/例子 → 放 `assets/`。

### 第 5 步：验证技能
- 确认 `SKILL.md` 存在且 front-matter 合法（`name` + `description` 两个键齐全、`name` 与目录名一致）。
- 运行 `python scripts/validate_skill.py <skills/<skill-name>>` 校验结构。
- 检查脚本可执行、路径正确、无 Python 语法错误。

## 编写高质量指令的原则

1. **具体可执行**：写"运行 `python scripts/x.py "关键词"`"，而不是"运行相关脚本"。
2. **给出模板**：报告/输出的格式用 Markdown 代码块给出示例。
3. **定义评价标准**：需要判断时，给出明确的阈值和正反面例子，避免主观。
4. **中英兼容**：触发词、示例同时覆盖中文与英文。
5. **自包含**：尽量不依赖外部 API Key；需要时用环境变量并在 SKILL.md 说明。

## 常用验证命令

```bash
# 校验单个技能的结构是否合法
python scripts/validate_skill.py ".cline/skills/<skill-name>"

# （如脚本用 Python）检查语法
python -m py_compile scripts/<script.py>
```

## 参考文件
- [references/skill-blueprint.md](references/skill-blueprint.md) — SKILL.md 逐节编写要点与完整示例
