# Web 技术栈适配模式

ui-ux-pro-max 给出建议时，可结合目标技术栈落地。以下为常见栈的实现提示。

## 原生 HTML + CSS

- 用 CSS 变量承载设计 Token（见《设计系统指南》最后一节）。
- 使用 `rem`/相对单位，基于 `html { font-size: 16px }`，保证缩放与可访问性。

## React (CSS Modules / inline style)

- 把 Token 放进 `:root` 变量或一份 `tokens.css`，通过 `var(--token)` 引用。
- 状态类（hover/focus/disabled）用伪类与 `aria-*`/`data-*` 属性表达，避免纯 JS 判断。

## Vue (scoped CSS)

- scoped 样式可直接用 `var(--token)` 引用全局变量，无需重复定义。
- 复用组件时保持 props 驱动、样式原子，便于统一设计系统。

## Tailwind CSS

- 在 `tailwind.config.js` 中映射 Token：`colors`、`spacing`(以 4px 基准)、`borderRadius`、`fontSize`。
- 示例：
  ```js
  module.exports = {
    theme: {
      extend: {
        colors: { primary: '#2563eb', muted: '#6b7280' },
        spacing: { 1: '4px', 2: '8px', 3: '12px', 4: '16px', 6: '24px', 8: '32px', 12: '48px' },
      },
    },
  };
  ```

## 组件库（Ant Design / Element Plus / MUI）

- 优先通过主题变量/`ConfigProvider`/`theme` 覆写其默认 Token，别逐个组件硬改样式。
- 覆盖时保持间距 Scale 与圆角档位一致，避免碎片化。
