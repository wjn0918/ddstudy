---
title: 使用
---

## 读取文件

```
String dataPath = "xx";

String content = new String(Files.readAllBytes(Paths.get(dataPath)));
```

## 打包/解压jar

jar -xvf test.jar

jar -cvf test.jar *

## 自定义函数式接口
```
    @FunctionalInterface
    interface UpdateFunc extends Serializable{
        void apply(SchoolETLConfig conf, String jobNo, String body);
    }


   public class UpdateXtszYh implements UpdateFunc{
        @Override
        public void apply(SchoolETLConfig conf, String psersonId, String body) {
            updateXtszYh(conf,psersonId,body,true);
        }
    }

    protected void updateCommon(UpdateFunc updateFunc){
        updateFunc.apply(conf,psersonId,body);

    }

     protected void updateXtszYh() {
        updateCommon(new UpdateXtszYh());

    }

```


## 安装
::: tabs

@tab centos

```
yum install -y java-1.8.0-openjdk.x86_64 java-1.8.0-openjdk-demo  java-1.8.0-openjdk-devel java-1.8.0-openjdk-javadoc
```

@tab ubuntu

```
sudo apt install -y openjdk-8-jdk
```

@tab 其他

:::



- 匿名类
创建子类对象时，除了使用父类地构造方法外还有类体，此类体被认为是一个子类去掉类声明后地类体，称为匿名类

没有显式地声明一个类地子类，又想使用子类创建一个对象
适合创建只需要一次使用地类


- 打包

```
jar -cf cs.jar -C . org\\example\\flume
```

- windows运行jar

```
java -cp nh-spark-1.0-SNAPSHOT-assembly.jar;D:\soft\spark-3.2.2-bin-hadoop3.2\jars\* -Dspark.master=local[4] -Dconf_file=prod -Doverwrite=flase cn.shingi.nh.NhSparkApplication --conf_file=prod
```


## service

```
[Unit]
Description=batch-server for shuqi server
After=network.target

[Service]
Type=forking
EnvironmentFile=/etc/sysconfig/shuqi/global.config
User=deploy
Group=deploy
LimitNOFILE=100000
LimitNPROC=65535
LimitMEMLOCK=infinity
WorkingDirectory=/opt/workspace/batch-server
PIDFile=/opt/workspace/batch-server/sbin/batch-server.pid
ExecStartPre=/usr/bin/bash /usr/local/bin/shuqi batch-server init
ExecStart=/usr/bin/bash /usr/local/bin/shuqi batch-server start
ExecStop=/usr/bin/bash  /usr/local/bin/shuqi batch-server stop
PrivateTmp=true
Restart=on-failure
RestartSec=40

[Install]
WantedBy=multi-user.target

```


## 排除某些字段序列化

```
private transient DruidDataSource sourceDS;
```