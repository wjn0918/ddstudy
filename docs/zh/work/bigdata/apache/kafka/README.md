---
title: kafka
---

## docker-compose

```
<!-- @include: ./doc/compose.yml -->
```


## docker

```
docker run -p 80:8080 -e DYNAMIC_CONFIG_ENABLED=true --name kafka-ui  provectuslabs/kafka-ui
```