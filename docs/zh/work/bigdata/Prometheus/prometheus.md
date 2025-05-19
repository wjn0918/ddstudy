---
title: Overview
---








[下载prometheus](https://prometheus.io/download/)  
[下载mysqld_exporter](https://prometheus.io/download/#mysqld_exporter)


nohup ./prometheus &

## mysqld_exporter
```


# 配置mysqld_exporter


```
vi .my.cnf

[client]
user=root
password=Mysql@2023
port=3306

```
# 启动mysqld_exporter
监控数据量大小
./mysqld_exporter --web.telemetry-path=/metrics --collect.info_schema.innodb_tablespaces
mysql_info_schema_innodb_tablespace_file_size_bytes


https://github.com/prometheus/mysqld_exporter






模糊查询使用 ~
mysql_info_schema_innodb_tablespace_file_size_bytes{instance="192.168.3.204:9104", job="mysql-105", tablespace_name=~"cs.*"}


# prometheus 配置

  - job_name: 'mysql-105'      # 给被监控主机取个名字
    static_configs:
    - targets: ['192.168.3.204:9104']      # 这里填写被监控主机的IP和端口

    
```
