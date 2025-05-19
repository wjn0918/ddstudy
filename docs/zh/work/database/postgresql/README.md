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



## 手工数据

with t as (
  select * from (
    values 
    ('1')
  ) as t (id)

)


## 备份数据

```
#!/bin/bash

# 数据库连接信息
DB_HOST="localhost"
DB_USER="postgres"
DB_NAME="postgres"

# 备份目录
BACKUP_DIR="/tmp"
TARGET_DIR="/data/backup/"

# 备份文件名格式：school_yyyymmdd.dump
BACKUP_FILE="$BACKUP_DIR/school_$(date +%Y%m%d).dump"

# 执行备份
docker exec -t pgsql_db_1 pg_dump -h $DB_HOST -U $DB_USER -F c -b -v -f $BACKUP_FILE $DB_NAME


docker cp pgsql_db_1:$BACKUP_FILE $TARGET_DIR



# 检查备份是否成功
if [ $? -eq 0 ]; then
  echo "备份成功: $BACKUP_FILE"
else
  echo "备份失败"
  exit 1
fi

# 删除7天前的备份文件
find $TARGET_DIR -name "school_*.dump" -type f -mtime +6 -exec rm -f {} \;

echo "旧备份文件清理完成"
```

0 2 * * * /data/backup/backup.sh >> /var/log/backup_school.log 2>&1