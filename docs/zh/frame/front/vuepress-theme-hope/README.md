---
title: vuepress-theme-hope
icon: lightbulb
---

## 配置

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
