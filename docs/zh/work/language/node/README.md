---
title: Node
---
<Catalog/>


## 启动一个简单服务

npm init -y

npm i vite

添加
```
"scripts": {
    "dev": "vite"
}

```

指定入口文件 vite.config.js

```

import { defineConfig } from 'vite';

export default defineConfig({
    server: {
        open: '/map.html' // 指定启动服务器时打开的页面
    },
    root: './', // 设置项目的根目录，默认是当前目录，这里明确指出是为了清晰
    build: {
        rollupOptions: {
            input: {
                main: './map.html', // 指定入口文件为 map.html
            }
        }
    }
});

```


## 安装

https://nodejs.org/dist/

wget https://nodejs.org/dist/v18.20.5/node-v18.20.5-linux-x64.tar.gz