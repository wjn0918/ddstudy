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
docker cp school-mysql:/var/lib/mysql data
docker cp school-mysql:/var/log/mysql logs
```


```
<!-- @include: compose.yml -->



```

@tab 手动
<!-- @include: install_manual.md -->

:::


<!-- <Catalog/> -->

```
docker exec -i school-mysql sh -c 'exec mysql -uroot -pMysqlWjn@2025 ' <<C 
> select 1 
> C
```


docker exec -i school-mysql sh -c 'exec mysql -uroot -p"Mysql"' < /some/path/on/your/host/all-databases.sql
