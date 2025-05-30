---
title: docker compose
---

## 使用dockercompose 直接build 

docker compose up --build

```
services:
  backend:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: easybd-api
    ports:
      - "5001:5001"
    networks:
      - easybd-network

  frontend:
    build:
      context: ./web
      dockerfile: Dockerfile
    container_name: easybd-frontend
    ports:
      - "3000:80"
    networks:
      - easybd-network
    depends_on:
      - backend

networks:
  easybd-network:
    driver: bridge

```


## 案例

### datax
<!-- #region datax -->
```
# Use postgres/example user/password credentials
version: '3.1'
services:
  datax:
    image: registry.cn-hangzhou.aliyuncs.com/wjn0918/soft:datax
    container_name: datax
    restart: always
    network_mode: "host"
    volumes:
      - ./job:/app/job
```
- 执行

```
docker exec -i datax sh -c 'python bin/datax.py job/job.json'
```

<!-- #endregion datax -->

### Zeppelin
<!-- #region Zeppelin -->
```
# Use postgres/example user/password credentials
version: '3.1'
services:
  datax:
    image: registry.cn-hangzhou.aliyuncs.com/wjn0918/soft:datax
    restart: always
    network_mode: "host"
```
<!-- #endregion Zeppelin -->


## 使用

执行多个命令

```
command: >
  sh -c "npm install && npm run build && npm run start"
```