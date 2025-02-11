---
title: VuePress
---


::: important
推荐选好主题然后进行初始化 [主题市场](https://marketplace.vuejs.press/zh/themes/docs.html)
:::

## [已有文档手动创建](https://v2.vuepress.vuejs.org/zh/guide/getting-started.html#%E5%88%9B%E5%BB%BA%E9%A1%B9%E7%9B%AE)

假设项目结构如下：
```
├─helloVuePress
│  └─docs
```

- 初始化项目

```
cd helloVuePress & git init & npm init
```

- 安装 VuePress

```
# 安装 vuepress
npm install -D vuepress@next
# 安装打包工具和主题
npm install -D @vuepress/bundler-vite@next @vuepress/theme-default@next
```

- 创建 docs 目录和 docs/.vuepress 目录

```
mkdir docs
mkdir docs/.vuepress
```

- 创建 VuePress 配置文件 docs/.vuepress/config.js

```
import { viteBundler } from '@vuepress/bundler-vite'
import { defaultTheme } from '@vuepress/theme-default'
import { defineUserConfig } from 'vuepress'

export default defineUserConfig({
  bundler: viteBundler(),
  theme: defaultTheme(),
})
```

- 启动开发服务器
package.json 中添加一些 scripts ：

```
{
  "scripts": {
    "docs:dev": "vuepress dev docs",
    "docs:build": "vuepress build docs"
  }
}
```

- 运行 docs:dev 脚本可以启动开发服务器:
```
npm run docs:dev
```


## 配置

### 更改端口

config.ts

```
export default defineUserConfig({
  port: '9999'

});
```