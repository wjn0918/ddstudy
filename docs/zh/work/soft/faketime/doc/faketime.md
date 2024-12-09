# 修改单个应用程序的系统时间

http://inorz.net/2018/03/26/modifies-the-system-time-for-a-single-application/



export LD_PRELOAD=/usr/local/lib/faketime/libfaketime.so.1 FAKETIME="2022-11-17 10:30:22" 


# 更改docker容器

需要更改mysql 容器来设置时间

```
docker run -dt \
      --net=host \
      --restart=always \
      --name $APP_NAME \
      -v ${basedir}/conf:/etc/mysql/conf.d/ \
      -v ${basedir}/data:/var/lib/mysql \
      -v ${basedir_home}:/home \
      -e MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD} \
      -v /usr/local/lib/faketime/libfaketime.so.1:/libfaketime.so.1 \
      --env LD_PRELOAD=/libfaketime.so.1 \
      --env FAKETIME="-243d" \
      ${DOCKER_IMAGE}

```



* 挂载脚本libfaketime.so.1
* 设置环境变量

docker run -dt \
  --net=host \
  --cap-drop SYS_TIME \
  --restart=always \
  --name $APP_NAME \
  --privileged \
  --env="TZ=UTC" \
  -v $basedir_app:/home \
  -v /usr/local/lib/faketime/libfaketime.so.1:/libfaketime.so.1 \
  --env LD_PRELOAD=/libfaketime.so.1 \
  --env FAKETIME="-100d" \
  ${DOCKER_IMAGE} \
  bash /home/bin/start_docker.sh


使用下述方式可以更改容器时间
export LD_PRELOAD=/usr/local/lib/faketime/libfaketime.so.1 FAKETIME="-100d" date