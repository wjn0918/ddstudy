---
title: docker使用
---

## 备份docker中的数据
```
#!/bin/bash

# 配置信息
DB_HOST="localhost"
DB_USER="postgres"
DB_NAME="postgres"
CONTAINER_NAME="pgsql_db_1"

# 目录配置
BACKUP_DIR="/tmp"
TARGET_DIR="/data/backup/"

# 创建目标目录（如果不存在）
mkdir -p "$TARGET_DIR"

# 生成备份文件名（带时间戳）
BACKUP_FILE="school_$(date +%Y%m%d_%H%M%S).dump"
FULL_BACKUP_PATH="$BACKUP_DIR/$BACKUP_FILE"
FULL_TARGET_PATH="$TARGET_DIR/$BACKUP_FILE"

# 执行备份
echo "开始数据库备份..."
docker exec -t "$CONTAINER_NAME" pg_dump -h "$DB_HOST" -U "$DB_USER" -F c -b -v -f "$FULL_BACKUP_PATH" "$DB_NAME"

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



## 镜像发布到阿里云


1. 登录阿里云Docker Registry
```
docker login --username=wjn_0918 registry.cn-hangzhou.aliyuncs.com
```
2. 从Registry中拉取镜像
```
docker pull registry.cn-hangzhou.aliyuncs.com/wjn0918/soft:[镜像版本号]
```
3. 将镜像推送到Registry
```
docker login --username=wjn_0918 registry.cn-hangzhou.aliyuncs.com
```
```
docker tag eb175b0743cc registry.cn-hangzhou.aliyuncs.com/wjn0918/soft:mysql-5.7.39
```
```
docker push registry.cn-hangzhou.aliyuncs.com/wjn0918/soft:[镜像版本号]
```


## 执行sql

```
docker exec -i mysql sh -c 'exec mysql -uroot -pMysql@2024 ' <<C 
> select 1 
> C

```

## 保存image

docker save zhaoolee-qs:1.0 > qs01.tar
docker load -i qso1.tar


## root用户登录 

docker exec -u 0 -it 


## 指定网络模式

容器与主机共享网络栈。这意味着容器将使用主机的IP地址和端口，而不是为容器单独分配的IP地址和端口
network_mode: "host"

# build image

> docker build -f Dockerfile* -t imagename .


# run container
> docker-compose -f xiny-school-gateway.yml up -d


# 查看磁盘卷位置：

```
docker volume ls

docker volume inspect jenkins_jenkins-data
```

# 容器东八区

```
volumes:
    - /etc/localtime:/etc/localtime
```
# 删除所有none镜像
docker rmi $(docker images | grep 'none' | awk '{print $3}')


# 删除停止的容器

docker rm $(docker ps -a -q)

# 调试dockerfile构建的镜像

```
  school-system-gateway:
    container_name: school-system-gateway
    image: school-system-gateway:0.0.1-SNAPSHOT
    entrypoint: 
      - tail
      - -f
      - /dev/null
```
docker exec -it 容器 /bin/sh


# 服务顺序启动
[参考](https://www.cnblogs.com/wang_yb/p/9400291.html)

docker-compose.yml 中添加
entrypoint: sh /app/system-gateway-0.0.1-SNAPSHOT/bin/entrypoint.sh -d nacos:8848 -c 'sh /app/system-gateway-0.0.1-SNAPSHOT/bin/start-gateway.sh';
-d 参数后面的多个服务和端口用逗号(,)隔开


```
#!/bin/bash
#set -x
#******************************************************************************
# @file    : entrypoint.sh
# @author  : wangyubin
# @date    : 2018-08- 1 10:18:43
#
# @brief   : entry point for manage service start order
# history  : init
#******************************************************************************

: ${SLEEP_SECOND:=2}

wait_for() {
    echo Waiting for $1 to listen on $2...
    while ! nc -z $1 $2; do echo waiting...; sleep $SLEEP_SECOND; done
}

declare DEPENDS
declare CMD

while getopts "d:c:" arg
do
    case $arg in
        d)
            DEPENDS=$OPTARG
            ;;
        c)
            CMD=$OPTARG
            ;;
        ?)
            echo "unkonw argument"
            exit 1
            ;;
    esac
done

for var in ${DEPENDS//,/ }
do
    host=${var%:*}
    port=${var#*:}
    wait_for $host $port
done

eval $CMD

```