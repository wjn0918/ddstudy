* 环境变量

HADOOP_HOME


hive-site.xml

```

```


```


wget https://downloads.mysql.com/archives/get/p/3/file/mysql-connector-java-8.0.16-1.el7.noarch.rpm

rpm -ivh mysql-connector-java-8.0.16-1.el7.noarch.rpm

# 初始化元数据
bin/schematool -dbType derby -initSchema
bin/schematool -dbType mysql -initSchema

# 启动服务
nohup bin/hive --service metastore &
nohup bin/hive --service hiveserver2 &
```

hiveserver2 需要root用户启动
