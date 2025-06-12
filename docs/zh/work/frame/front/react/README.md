---
title: React
---
基于 Vite 的 React + TypeScript 项目

```
npm create vite@latest web --template react-ts

```

```
npm create vite@latest web -- --template react-ts
```

```
npm install --save-dev @types/node
```



## 项目结构

```
my-app/
├── public/
├── src/
│   ├── assets/                # 静态资源（图片、图标、全局样式等）
│   ├── components/            # 通用组件（按钮、表格、弹窗等）
│   ├── features/              # 业务模块，每个模块一个目录
│   │   └── stocks/            # 示例：股票模块
│   │       ├── api.ts         # API 请求函数（对应 FastAPI 后端）
│   │       ├── StockList.tsx  # 组件：股票列表
│   │       └── types.ts       # 类型定义（如 Stock 类型）
│   ├── hooks/                 # 自定义 Hook（如 useStocks）
│   ├── layouts/               # 页面布局（如后台框架、导航栏）
│   ├── pages/                 # 路由页面（可与 features 分开）
│   │   └── Home.tsx
│   ├── router/                # 路由配置（React Router v6）
│   ├── services/              # 接口封装层（可选，统一调用 fetch/axios）
│   ├── store/                 # 状态管理（Redux/Zustand/Recoil）
│   ├── utils/                 # 工具函数（如格式化、日期处理等）
│   ├── App.tsx
│   ├── main.tsx               # 项目入口
│   └── vite-env.d.ts
├── .env
├── index.html
├── package.json
├── tsconfig.json
└── vite.config.ts

```