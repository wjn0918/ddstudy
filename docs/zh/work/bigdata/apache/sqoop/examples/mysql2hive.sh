# orc 格式的hive表

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