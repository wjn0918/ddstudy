* 配置hadoop jar地址

```
export HADOOP_HOME=${HADOOP_HOME}
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export SPARK_DIST_CLASSPATH=$($HADOOP_HOME/bin/hadoop classpath)
```

* 配置hive 地址

hive-site.xml 复制到conf目录下

* 配置 spark-default.conf

```
spark.sql.legacy.createHiveTableByDefault = false
spark.sql.warehouse.dir hdfs://192.168.3.204:9000/user/hive/warehouse
```

* java.lang.IllegalArgumentException: Directory /data/disk_01/hive/jdbc is not allowed for addJar