---
title: vuepress-theme-hope
icon: lightbulb
---

## [创建项目](https://theme-hope.vuejs.press/zh/guide/intro/install.html)

```
npm init vuepress-theme-hope@latest add [dir]
```


## 支持图标



Iconify: https://icon-sets.iconify.design/
Iconfont: https://www.iconfont.cn/
默认使用  Fontawesome: https://fontawesome.com/search?o=r&m=free

## [github pages](https://theme-hope.vuejs.press/zh/get-started/deploy.html#%E6%9E%84%E5%BB%BA%E9%A1%B9%E7%9B%AE)

::: important

```
如果你的仓库地址是一个普通的形如 https://github.com/<USERNAME>/<REPO> 的格式，
网站将会被发布到 https://<USERNAME>.github.io/<REPO>/ ，
也就是说，你需要将 base 设置为 "/<REPO>/"
```


:::



## 配置


### [提示](https://theme-hope.vuejs.press/zh/guide/markdown/stylize/hint.html)

```
::: important
重要容器。
:::

::: info
信息容器。
:::

::: note
注释容器。
:::

::: tip
提示容器
:::

::: warning
警告容器
:::

::: caution
危险容器
:::

::: details
详情容器
:::
```


### [选项卡](https://theme-hope.vuejs.press/zh/guide/markdown/content/tabs.html)

```
::: tabs

@tab 标题 1

<!-- tab 1 内容 -->

@tab 标题 2

<!-- tab 2 内容 -->

<!-- 👇 tab 3 将会被默认激活 -->

@tab:active 标题 3

<!-- tab 3 内容 -->

:::

```


### [navbar](https://theme-hope.vuejs.press/zh/guide/layout/navbar.html)

- 设置分组

```
 {
    text: "框架",
    prefix: "zh/frame/",
    children: [
      {
        text: "前端",
        prefix: "front/",
        children: [
          "vuepress-theme-hope/"
        ]
      },
      {
        text: "web",
        prefix: "web/",
        children: [
          "spring/"
        ]
      }
    ]
  },

```


### [sidebar](https://theme-hope.vuejs.press/zh/guide/layout/sidebar.html)

- 多个侧边栏

```
"/zh/reading/demo/":"structure",
"/zh/reading/zootopia/":"structure",
```


## MarkDown
### [导入文件](https://theme-hope.vuejs.press/zh/guide/markdown/content/include.html#%E9%85%8D%E7%BD%AE)

- 配置

```
import { defineUserConfig } from "vuepress";
import { hopeTheme } from "vuepress-theme-hope";

export default defineUserConfig({
  theme: hopeTheme({
    markdown: {
      include: true,
    },
  }),
});
```

- 语法

使用 `<!-- @include: filename -->` 导入文件。

如果要部分导入文件，你可以指定导入的行数

`<!-- @include: filename{start-end} -->`
`<!-- @include: filename{start-} -->`
`<!-- @include: filename{-end} -->`
同时你也可以导入文件区域:

`<!-- @include: filename#region -->`
