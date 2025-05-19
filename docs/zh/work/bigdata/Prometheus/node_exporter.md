---
title: node_exporter
---


## [node_exporter](https://prometheus.io/download/#node_exporter)


### cpu、内存相关的指标
node_load1     过去 1 分钟的系统平均负载。
node_memory_MemTotal_bytes  系统总内存量（以字节为单位）。
node_memory_MemAvailable_bytes   系统当前可用的内存量（以字节为单位）。
node_memory_Cached_bytes          系统缓存使用的内存（以字节为单位）。
node_memory_Buffers_bytes          用于缓冲使用的内存（以字节为单位）。
计算可用内存百分比： node_memory_MemAvailable_bytes /
node_memory_MemTotal_bytes * 100
计算已用内存百分比：(node_memory_MemTotal_bytes -
node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes *100

### 磁盘相关指标

node_filesystem_size_bytes   文件系统大小（以字节为单位）。
node_filesystem_avail_bytes   文件系统可用空间（以字节为单位）
计算可用空间百分比： node_filesystem_avail_bytes /
node_filesystem_size_bytes * 100

计算已用空间百分比：(node_filesystem_size_bytes -
node_filesystem_avail_bytes ) / node_filesystem_size_bytes * 100