---
title: docker compose 案例
---

## datax

```
# Use postgres/example user/password credentials
version: '3.1'
services:
  datax:
    image: registry.cn-hangzhou.aliyuncs.com/wjn0918/soft:datax
    restart: always
    network_mode: "host"
```

## Zeppelin
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
