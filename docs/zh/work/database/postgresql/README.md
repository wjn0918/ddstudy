---
title: Postgresql
---

## 安装

::: tabs

@tab docker compose
```
# Use postgres/example user/password credentials
version: '3.1'
services:
  db:
    image: postgres:13
    restart: always
    network_mode: "host"
    environment:
      POSTGRES_PASSWORD: Pgsql@2024
      TZ: Asia/Shanghai
    volumes:
      - ./data:/var/lib/postgresql/data
  adminer:
    image: adminer
    restart: always
    ports:
      - 8090:8080
```

:::


<Catalog />


