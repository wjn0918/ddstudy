---
title: Rules
---


```

groups:
- name: Hosts.rules
  rules:
  ## Custom By wangshui
  - alert: HostDown
    expr: up{job=~"node-exporter|prometheus|grafana|alertmanager"} == 0
    for: 0m
    labels:
      severity: critical
    annotations:
      title: 'Instance down'
      description: "主机: 【{{ $labels.instance }}】has been down for more than 1 minute"

  - alert: HostCpuLoadAvage
    expr: sum(node_load5) by (instance) > 10
    for: 1m
    annotations:
      title: "5分钟内CPU负载过高"
      description: "主机: 【{{ $labels.instance }}】 5五分钟内CPU负载超过10 (当前值：{{ $value }})"
    labels:
      severity: 'warning'

  - alert: HostCpuUsage
    expr: (1-((sum(increase(node_cpu_seconds_total{mode="idle"}[5m])) by (instance))/ (sum(increase(node_cpu_seconds_total[5m])) by (instance))))*100 > 80
    for: 1m
    annotations:
      title: "CPU使用率过高"
      description: "主机: 【{{ $labels.instance }}】 5五分钟内CPU使用率超过80% (当前值：{{ $value }})"
    labels:
      severity: 'warning'

  - alert: HostMemoryUsage
    expr: (1-((node_memory_Buffers_bytes + node_memory_Cached_bytes + node_memory_MemFree_bytes)/node_memory_MemTotal_bytes))*100 > 80
    for: 1m
    annotations:
      title: "主机内存使用率超过80%"
      description: "主机: 【{{ $labels.instance }}】 内存使用率超过80% (当前使用率：{{ $value }}%)"
    labels:
      severity: 'warning'

  - alert: HostIOWait
    expr: ((sum(increase(node_cpu_seconds_total{mode="iowait"}[5m])) by (instance))/(sum(increase(node_cpu_seconds_total[5m])) by (instance)))*100 > 10
    for: 1m
    annotations:
      title: "磁盘负载过高"
      description: "主机: 【{{ $labels.instance }}】 5五分钟内磁盘负载过高 (当前负载值：{{ $value }})"
    labels:
      severity: 'warning'

  - alert: HostFileSystemUsage
    expr: (1-(node_filesystem_free_bytes{fstype=~"ext4|xfs",mountpoint!~".*tmp|.*boot" }/node_filesystem_size_bytes{fstype=~"ext4|xfs",mountpoint!~".*tmp|.*boot" }))*100 > 70
    for: 1m
    annotations:
      title: "磁盘空间剩余不足"
      description: "主机: 【{{ $labels.instance }}】 {{ $labels.mountpoint }}分区使用率超过70%, 当前值使用率：{{ $value }}%"
    labels:
      severity: 'warning'

  - alert: HostSwapIsFillingUp
    expr: (1 - (node_memory_SwapFree_bytes / node_memory_SwapTotal_bytes)) * 100 > 80
    for: 2m
    labels:
      severity: 'warning'
    annotations:
      title: "主机swap分区不足"
      description: "主机: 【{{ $labels.instance }}】 swap分区使用超过 (>80%), 当前值使用率: {{ $value }}%"

  - alert: HostNetworkConnection-ESTABLISHED
    expr:  sum(node_netstat_Tcp_CurrEstab) by (instance) > 1000
    for: 5m
    labels:
      severity: 'warning'
    annotations:
      title: "主机ESTABLISHED连接数过高"
      description: "主机: 【{{ $labels.instance }}】 ESTABLISHED连接数超过1000, 当前ESTABLISHED连接数: {{ $value }}"

  - alert: HostNetworkConnection-TIME_WAIT
    expr:  sum(node_sockstat_TCP_tw) by (instance) > 1000
    for: 5m
    labels:
      severity: 'warning'
    annotations:
      title: "主机TIME_WAIT连接数过高"
      description: "主机: 【{{ $labels.instance }}】 TIME_WAIT连接数超过1000, 当前TIME_WAIT连接数: {{ $value }}"

  - alert: HostUnusualNetworkThroughputIn
    expr:  sum by (instance, device) (rate(node_network_receive_bytes_total{device=~"ens.*"}[2m])) / 1024 / 1024 > 100
    for: 5m
    labels:
      severity: 'warning'
    annotations:
      title: "主机网卡入口流量过高"
      description: "主机: 【{{ $labels.instance }}】, 网卡: {{ $labels.device }} 入口流量超过 (> 100 MB/s), 当前值: {{ $value }}"

  - alert: HostUnusualNetworkThroughputOut
    expr: sum by (instance, device) (rate(node_network_transmit_bytes_total{device=~"ens.*"}[2m])) / 1024 / 1024 > 100
    for: 5m
    labels:
      severity: 'warning'
    annotations:
      title: "主机网卡出口流量过高"
      description: "主机: 【{{ $labels.instance }}】, 网卡: {{ $labels.device }} 出口流量超过 (> 100 MB/s), 当前值: {{ $value }}"

  - alert: HostUnusualDiskReadRate
    expr: sum by (instance, device) (rate(node_disk_read_bytes_total{device=~"sd.*"}[2m])) / 1024 / 1024 > 50
    for: 5m
    labels:
      severity: 'warning'
    annotations:
      title: "主机磁盘读取速率过高"
      description: "主机: 【{{ $labels.instance }}】, 磁盘: {{ $labels.device }} 读取速度超过(50 MB/s), 当前值: {{ $value }}"

  - alert: HostUnusualDiskWriteRate
    expr: sum by (instance, device) (rate(node_disk_written_bytes_total{device=~"sd.*"}[2m])) / 1024 / 1024 > 50
    for: 2m
    labels:
      severity: 'warning'
    annotations:
      title: "主机磁盘写入速率过高"
      description: "主机: 【{{ $labels.instance }}】, 磁盘: {{ $labels.device }} 写入速度超过(50 MB/s), 当前值: {{ $value }}"

  - alert: HostOutOfInodes
    expr: node_filesystem_files_free{fstype=~"ext4|xfs",mountpoint!~".*tmp|.*boot" } / node_filesystem_files{fstype=~"ext4|xfs",mountpoint!~".*tmp|.*boot" } * 100 < 10
    for: 2m
    labels:
      severity: 'warning'
    annotations:
      title: "主机分区Inode节点不足"
      description: "主机: 【{{ $labels.instance }}】 {{ $labels.mountpoint }}分区inode节点不足 (可用值小于{{ $value }}%)"

  - alert: HostUnusualDiskReadLatency
    expr: rate(node_disk_read_time_seconds_total{device=~"sd.*"}[1m]) / rate(node_disk_reads_completed_total{device=~"sd.*"}[1m]) > 0.1 and rate(node_disk_reads_completed_total{device=~"sd.*"}[1m]) > 0
    for: 2m
    labels:
      severity: 'warning'
    annotations:
      title: "主机磁盘Read延迟过高"
      description: "主机: 【{{ $labels.instance }}】, 磁盘: {{ $labels.device }} Read延迟过高 (read operations > 100ms), 当前延迟值: {{ $value }}ms"

  - alert: HostUnusualDiskWriteLatency
    expr: rate(node_disk_write_time_seconds_total{device=~"sd.*"}[1m]) / rate(node_disk_writes_completed_total{device=~"sd.*"}[1m]) > 0.1 and rate(node_disk_writes_completed_total{device=~"sd.*"}[1m]) > 0
    for: 2m
    labels:
      severity: 'warning'
    annotations:
      title: "主机磁盘Write延迟过高"
      description: "主机: 【{{ $labels.instance }}】, 磁盘: {{ $labels.device }} Write延迟过高 (write operations > 100ms), 当前延迟值: {{ $value }}ms"

```