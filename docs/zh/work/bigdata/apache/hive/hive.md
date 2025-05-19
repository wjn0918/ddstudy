---
title: 常用操作
---


## HCatalog

HCatalog 提供了一个统一的元数据服务，允许不同的工具如 Pig、MapReduce 等通过 HCatalog 直接访问存储在 HDFS 上的底层文件



* 刷新元数据

hive -e "msck repair table demo.t_1;"


## 变量查询

select "${hiveconf:hive.execution.engine}";


## 分区有数据查不到

MSCK REPAIR TABLE t_cs;

## 快速启动

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
