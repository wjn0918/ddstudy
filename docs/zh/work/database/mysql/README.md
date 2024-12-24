---
title: Mysql
---

## 安装



:::tabs

@tab docker compose

- 先注释掉配置文件的映射
- 将配置文件复制到本地
- 解除注释重启容器

```
docker compose up
docker cp school-mysql:/etc/mysql conf
```


```
<!-- @include: compose.yml -->



```

@tab 手动
<!-- @include: install_manual.md -->

:::


<!-- <Catalog/> -->