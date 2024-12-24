---
title: docker使用
---


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