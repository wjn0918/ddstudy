---
title: vue
---

* vue3 添加路由和静态资源前缀

```

import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
 
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  }
]
 
const router = createRouter({
  history: createWebHistory('/your-prefix/'),  // 设置前缀
  routes
})
 

```