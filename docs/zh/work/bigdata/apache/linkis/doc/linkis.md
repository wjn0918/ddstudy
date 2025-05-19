mysql 5.7




yum install -y  java-1.8.0-openjdk.x86_64 java-1.8.0-openjdk-demo  java-1.8.0-openjdk-devel java-1.8.0-openjdk-javadoc


hadoop/common/lib/*  复制到 lib/linkis-commons/public-module/


useradd hadoop -g hadoop

echo "hadoop ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

* 配置nacos

mvn clean install -DskipTests -Ddiscovery=nacos

To configure during installation (deploy-config/linkis-env.sh):

DISCOVERY=NACOS
NACOS_SERVER_ADDR=127.0.0.1:8848



* 
yum install -y telnet dos2unix unzip zip expect lsof


db.sh 设置

HIVE_META_URL="jdbc:mysql://172.23.0.200:3306/metastore?useUnicode=true&characterEncoding=UTF-8"
HIVE_META_USER="root"
HIVE_META_PASSWORD="Mysql@2023"




* HADOOP_CONF_DIR


hadoop-common 3.3.4


woodstox-core-5.0.3.jar和stax2-api-3.1.4.jar







# error

* JDOPersistenceManagerFactory was not found

这是因为缺少一些依赖包，我们找到相应的包拷贝到Linkis的插件hive中即可
位置：LinkisInstall/lib/linkis-engineconn-plugins/hive/dist/vx.x.x/lib）
类似还有缺少一些别的依赖包
缺少的jar：datanucleus-api-jdo-x.x.x.jar、datanucleus-rdbms-x.x.x.jar、javax.jdo-x.x.x-m3.jar、jdo-api-x.x.x.jar  HikariCP-2.6.1.jar
这里xxx对应自己用的版本号即可


https://blog.csdn.net/cxh6863/article/details/123620481


* 使用root 启动可以，使用hadoop  报Client not connected, current status:STARTING


* 无法获取Yarn信息

linkis_cg_rm_external_resource_provider





# 部署


* mg-gateway

```
export LINKIS_COMMONS_LIB=$LINKIS_HOME/$LINKIS_PUBLIC_MODULE
## set class path
export SERVER_CLASS_PATH=$SERVER_CONF_PATH:$SERVER_LIB/*:$LINKIS_EXTENDED_LIB/*:$LINKIS_COMMONS_LIB/*
```

* cg-engineconnmanager

nacos 注册报错  需要添加

application-engineconn.yml

```
nacos:
  discovery:
    server-addr: server211.bd:8848

```