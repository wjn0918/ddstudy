# 环境

```
export DATAX_HOME=/usr/local/datax
export PYTHON_HOME=/usr
export SQOOP_HOME=/usr/local/sqoop
export HADOOP_HOME=/usr/local/hadoop
export HIVE_HOME=/usr/local/hive
export PATH=$PATH:$DATAX_HOME/bin:$PYTHON_HOME/bin:$SQOOP_HOME/bin:$HADOOP_HOME/bin:$HIVE_HOME/hcatalog/bin

HADOOP_CLASSPATH=$(hcat -classpath) 
export HADOOP_CLASSPATH
```


# sqoop_node_demo

```
sqoop import \
--connect jdbc:mysql://localhost:3306/demo?useSSL=false \
--username demo \
--password Demo@2023 \
--table t_1 \
--delete-target-dir \
--hive-home /usr/local/hive \
--hcatalog-database datax \
--hcatalog-table t_1 \
--hcatalog-partition-keys dt \
--hcatalog-partition-values 20230606 \
-m 1
```