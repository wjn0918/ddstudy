---
title: Q&A
---

* 在ts+vite项目中使用path模块提示错误

path模块是node.js内置的功能，但是node.js本身并不支持typescript，所以直接在typescript项目里使用是不行的

```
npm install @types/node
```

* react + ts 配置项目路劲别名（import的时候使用@符号报错）

tsconfig.app.json 新增如下内容

```
"compilerOptions": {
	...
	"baseUrl": "./",
	"paths": {
	  "@/*": [
	    "src/*"
	  ]
	}
},
```