---
name: ui-ux-pro-max
description: >
  Professional UI/UX design guidance and implementation support for web/frontend work. Use when the user asks to
  design a screen or page, improve visual hierarchy, pick a color palette or spacing scale, review a UI, ensure
  accessibility (WCAG contrast), build with a design system, 设计一个页面/界面，优化 UI，调整配色/间距/排版，
  审查界面，提升用户体验，保持设计一致性.
---

# UI/UX Pro Max — 专业界面设计引导

提供一套可执行的前端界面设计方法论：从澄清需求、建立设计 Token，到布局、组件、视觉规范、可访问性与交付评审。适用于 React/Vue/原生 HTML 等各类前端项目。

## 什么时候使用

- 需要**从零设计一个页面/组件**的视觉与交互。
- 需要**优化现有 UI**（层次、配色、间距、排版）。
- 需要**检查可访问性/色彩对比度**。
- 需要**在多个页面间保持设计一致性**（设计系统 / Design Token）。

## 核心工作流

### 第 1 步：澄清需求（必要时提问）
明确：目标用户、使用场景、关键操作（CTA）、屏幕尺寸/设备、技术栈（React/Vue/HTML+CSS/Tailwind 等）、以及是否有已有设计规范。

### 第 2 步：确立设计 Token（一次定好，处处复用）
| Token | 建议做法 |
|-------|----------|
| 色彩 | 主色 / 强调色 / 语义色（成功、警告、错误）/ 中性色（背景、文字、边框）；主色选择有足够中明度，避免高饱和刺眼 |
| 间距 | 使用 4px 基准的 Scale：4 / 8 / 12 / 16 / 24 / 32 / 48 |
| 圆角 | 统一档位：sm(4) md(8) lg(12) full(圆形) |
| 字体 | 正文 14–16px；标题用清晰的层级（如 20/24/28）；行高正文 ≥1.5 |
| 阴影 | 一档轻、一档重，仅用于浮起层级 |
| 宽度 | 内容最大宽度（如 1200px），栅格 12 列 |

### 第 3 步：确定布局与层次（视觉金字塔）
- 通过**尺寸、颜色深浅、留白、字重**来构建主次关系，一个页面明确一个视觉焦点。
- 对比度优先于装饰：关键信息用高对比表现。
- 遵循邻近原则（Gestalt）：相关内容间距更近。

### 第 4 步：组件级规范
- 按钮、输入框、卡片、弹窗等组件保持一致的 padding、圆角、hover/active 状态。
- 状态可见：加载、空态、错误、成功都要有对应视觉反馈。

### 第 5 步：可访问性（a11y）校验
- 文字与背景对比度达到 WCAG AA（正文 ≥ 4.5:1，大字 ≥ 3:1）。用脚本校验：
  ```bash
  python scripts/contrast_check.py --fg "#333333" --bg "#ffffff"
  ```
- 可点击区域 ≥ 44×44px；仅用颜色表达状态时补充图标或文字。
- 交互元素保证键盘可达（focus 状态可见）。

### 第 6 步：交付与自检
- 输出时提供清晰的 CSS 变量 / Design Token 值，便于实现。
- 用下面的自检清单过一遍再交付。

## 交付自检清单

- [ ] 有 4px 基准的间距 Scale，且被一致使用
- [ ] 色彩主次分明，正文/背景对比度达标（可用脚本验证）
- [ ] 一个页面只有 1 个主要视觉焦点
- [ ] 各组件状态（hover/focus/disabled/error）齐全
- [ ] CTA 明确、层级突出
- [ ] 文本层级清晰（标题/正文/辅助文字有差异）
- [ ] 移动端与桌面端都有考虑

## 参考文件
- [references/design-system-guide.md](references/design-system-guide.md) — 设计 Token 详解、色彩公式、间距与排版规范
- 技术栈模式见 [data/stacks/web-stack-patterns.md](data/stacks/web-stack-patterns.md)
