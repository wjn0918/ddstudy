


# HCatalog

HCatalog 提供了一个统一的元数据服务，允许不同的工具如 Pig、MapReduce 等通过 HCatalog 直接访问存储在 HDFS 上的底层文件



* 刷新元数据

hive -e "msck repair table demo.t_1;"


# 变量查询

select "${hiveconf:hive.execution.engine}";


# 分区有数据查不到

MSCK REPAIR TABLE t_cs;