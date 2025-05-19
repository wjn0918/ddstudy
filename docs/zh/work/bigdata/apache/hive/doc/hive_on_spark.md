# 版本

hive  | spark
-|-
3.1.3|2.3.4



HIVE-27068
https://github.com/apache/hive/pull/4052/files




1. 配置SPARK_HOME环境变量
2. 更改spark配置
```
spark.master                     yarn
spark.eventLog.enabled           true
spark.eventLog.dir               hdfs://192.168.3.204:9000/user/spark/log
```

3. 更改hive配置

```
  <property>
    <name>hive.execution.engine</name>
    <value>spark</value>
  </property>

  <property>
    <name>spark.yarn.jars</name>
    <value>hdfs://192.168.3.204:9000/user/spark/jars/*</value>
</property>

```

4. 上传sparkjars

注意移除hive相关的


hdfs dfs -put * /user/spark/jars/
hdfs dfs -rm -f /user/spark/jars/hive*















*  java.lang.NoSuchFieldError: SPARK_RPC_SERVER_ADDRESS

因为spark打包时加了hive依赖，尝试使用没有hive的包

* ClassNotFoundException: org.apache.spark.AccumulatorParam
hive 和spark 版本不兼容




* ExecutionException: javax.security.sasl.SaslException: Client closed before SASL negotiation finished.

```
<property>
        <name>hive.spark.client.connect.timeout</name>
        <value>10000</value>
</property>
<property>
        <name>hive.spark.client.server.connect.timeout</name>
        <value>90000</value>
</property>

```
