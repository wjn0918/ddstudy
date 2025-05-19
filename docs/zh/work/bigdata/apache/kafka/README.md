---
title: kafka
---

::: warning
必须更改kafka日志目录
:::


## docker-compose

```
<!-- @include: ./doc/compose.yml -->
```


## docker

```
docker run -p 80:8080 -e DYNAMIC_CONFIG_ENABLED=true --name kafka-ui  provectuslabs/kafka-ui
```

## 使用

* 查看消费进度

./bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group streaming

* 重置偏移量

./bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group streaming --reset-offsets --topic sxt-b-x-in --to-datetime 2025-03-14T00:00:00.000 --execute

## 日志一直输出debug
查看是否有logback日志包