---
title: 案例
icon: lightbulb
---

## 数据备份
```
#!/bin/bash

# 配置信息
DB_HOST="localhost"
DB_USER="postgres"
DB_NAME="postgres"
CONTAINER_NAME="pgsql_db_1"

# 要排除的表（多个表用空格分隔）
EXCLUDE_TABLES=("t_1")

# 目录配置
BACKUP_DIR="/tmp"
TARGET_DIR="/data/backup/"

# 创建目标目录（如果不存在）
mkdir -p "$TARGET_DIR"

# 生成备份文件名（带时间戳）
BACKUP_FILE="school_$(date +%Y%m%d_%H%M%S).dump"
FULL_BACKUP_PATH="$BACKUP_DIR/$BACKUP_FILE"
FULL_TARGET_PATH="$TARGET_DIR/$BACKUP_FILE"

# 构造 pg_dump 排除表的参数
EXCLUDE_OPTIONS=""
for table in "${EXCLUDE_TABLES[@]}"; do
  EXCLUDE_OPTIONS+=" --exclude-table=\"$table\""
done

# 执行备份（排除多张表）
echo "开始数据库备份（排除表: ${EXCLUDE_TABLES[*]}）..."
docker exec -t "$CONTAINER_NAME" pg_dump -h "$DB_HOST" -U "$DB_USER" -F c -b -v \
  $EXCLUDE_OPTIONS \
  -f "$FULL_BACKUP_PATH" "$DB_NAME"

# 检查备份是否成功
if [ $? -ne 0 ]; then
  echo "错误：数据库备份失败"
  exit 1
fi

# 将备份文件从容器复制到宿主机
echo "正在传输备份文件..."
docker cp "$CONTAINER_NAME:$FULL_BACKUP_PATH" "$FULL_TARGET_PATH"

if [ $? -ne 0 ]; then
  echo "错误：备份文件传输失败"
  exit 1
fi

# 删除容器内的备份文件
echo "清理容器内临时备份文件..."
docker exec "$CONTAINER_NAME" rm -f "$FULL_BACKUP_PATH"

# 清理旧备份（保留7天）
echo "清理7天前的旧备份..."
find "$TARGET_DIR" -name "school_*.dump" -type f -mtime +6 -exec rm -f {} \;

# 输出备份信息
echo "备份成功完成"
echo "备份文件位置: $FULL_TARGET_PATH"
echo "文件大小: $(du -h "$FULL_TARGET_PATH" | cut -f1)"
```

## update

```

UPDATE t_vehicle_bike_info AS t
SET phone = t1.phone
FROM (
    select job_no from t_vehicle_bike_info where deleted= 0 and phone = ''
) AS t2
LEFT JOIN (
    select job_no, phone from t_info_student where workspace_id = 'HZBB' and phone != ''
) AS t1 on t2.job_no = t1.job_no
WHERE t.job_no = t2.job_no
```


select client_addr, count(1) from pg_stat_activity group by client_addr



show max_connections;


alter system set max_connections=1000;