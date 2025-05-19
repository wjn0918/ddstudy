---
title: 安装
---


::: tabs

@tab yum 方式安装

配置yum源：
> wget  -O  /etc/yum.repos.d/jenkins.repo  http://pkg.jenkins-ci.org/redhat/jenkins.repo

导入rpm密钥：
> rpm  --import  https://jenkins-ci.org/redhat/jenkins-ci.org.key

安装：
> yum  -y  install  jenkins --nogpgcheck

启动服务：
> systemctl  start  jenkins

访问网址：
xx.xx.xx.xx:8080
根据提示进行安装


## 更新 update-center

将url修改为 https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/current/update-center.json


清华
https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/update-center.json

阿里云镜像：
https://mirrors.aliyun.com/jenkins/updates/update-center.json

## 更新 下载地址
cd $JENKINS_HOME(默认地址： /var/lib/jenkins)

清华源
sed -i 's/http:\/\/updates.jenkins-ci.org\/download/https:\/\/mirrors.tuna.tsinghua.edu.cn\/jenkins/g' default.json && sed -i 's/http:\/\/www.google.com/https:\/\/www.baidu.com/g' default.json
阿里源
sed -i 's/http:\/\/updates.jenkins-ci.org\/download/https:\/\/mirrors.aliyun.com\/jenkins/g' default.json && sed -i 's/http:\/\/www.google.com/https:\/\/www.baidu.com/g' default.json

@tab docker-compose

```
version: '3.1'
services:
  jenkins:
    image: jenkins/jenkins:lts-jdk11
    volumes:
      - /data/jenkins/:/var/jenkins_home
      - /var/run/docker.sock:/var/run/docker.sock
      - /usr/bin/docker:/usr/bin/docker
      - /usr/lib/x86_64-linux-gnu/libltdl.so.7:/usr/lib/x86_64-linux-gnu/libltdl.so.7
    ports:
      - "8080:8080"
    expose:
      - "8080"
      - "50000"
    privileged: true
    user: root
    restart: always
    container_name: jenkins
    environment:
      JAVA_OPTS: '-Djava.util.logging.config.file=/var/jenkins_home/log.properties'
```
:::




