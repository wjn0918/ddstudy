# 宿主机创建数据存放目录映射到容器
mkdir -p /home/docker/db/mysql5.7/data

# 宿主机创建配置文件目录映射到容器 
mkdir -p /home/docker/db/mysql5.7/conf #(需要在此目录下创建"conf.d"、"mysql.conf.d"两个目录)
mkdir -p /home/docker/db/mysql5.7/conf/conf.d # (建议在此目录创建my.cnf文件并进行相关MySQL配置)
mkdir -p /home/docker/db/mysql5.7/conf/mysql.conf.d

# 宿主机创建日志目录映射到容器
mkdir -p /home/docker/db/mysql5.7/logs



# mysql 8

```
version: '3'
services:
  mysql:
    image: mysql:8
    container_name: mysql8
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: Mysql@2023
    ports:
      - "3307:3306"
    volumes:
      - ./data:/var/lib/mysql

```