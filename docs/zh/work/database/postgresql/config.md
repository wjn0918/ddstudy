---
title: 配置
icon: lightbulb
---




## 更改时区
data/postgresql.conf

log_timezone = 'Asia/Shanghai'
timezone = 'Asia/Shanghai'


```
# Use postgres/example user/password credentials
version: '3.1'
services:
  db:
    image: postgres:13
    restart: always
    network_mode: "host"
    environment:
      POSTGRES_PASSWORD: Pgsql@2024
      TZ: Asia/Shanghai
    volumes:
      - ./data:/var/lib/postgresql/data
  adminer:
    image: adminer
    restart: always
    ports:
      - 8090:8080

```

## 主备配置

### 修改配置

patronictl -c /etc/patroni.yml edit-config


shared_buffers: 31GB


SHOW shared_buffers;



* 使用patroni 初始化数据库

https://developer.aliyun.com/article/775029

```

sudo yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
sudo yum install -y postgresql13-server
sudo systemctl enable postgresql-13
sudo systemctl start postgresql-13

```
### root 用户安装

yum install -y python3 python3-pip python3-psycopg2 python3-devel
pip3 install patroni
pip3 install patroni[zookeeper]

vi /etc/patroni.yml
* 数据目录需要归属于postgres

patroni /etc/patroni.yml


```
scope: pgsql
namespace: /service/
name: pg1

restapi:
  listen: 0.0.0.0:8008
  connect_address: 192.168.33.10:8008

zookeeper:
    hosts: 192.168.33.10:2181,192.168.33.11:2181  # Zookeeper 集群地址

bootstrap:
  dcs:
    ttl: 30
    loop_wait: 10
    retry_timeout: 10
    maximum_lag_on_failover: 1048576
    master_start_timeout: 300
    synchronous_mode: true
    postgresql:
      use_pg_rewind: true
      use_slots: true
      parameters:
        listen_addresses: "0.0.0.0"
        port: 5432
        wal_level: logical
        hot_standby: "on"
        wal_keep_segments: 100
        max_wal_senders: 10
        max_replication_slots: 10
        wal_log_hints: "on"

  initdb:
  - encoding: UTF8
  - locale: C
  - lc-ctype: zh_CN.UTF-8
  - data-checksums

  pg_hba:
  - host replication repl 0.0.0.0/0 md5
  - host all all 0.0.0.0/0 md5

postgresql:
  listen: 0.0.0.0:5432
  connect_address: 192.168.33.10:5432
  data_dir: /var/lib/pgsql/13/data
  bin_dir: /usr/pgsql-13/bin

  authentication:
    replication:
      username: repl
      password: "123456"
    superuser:
      username: postgres
      password: "123456"

  basebackup:
    max-rate: 100M
    checkpoint: fast

tags:
    nofailover: false
    noloadbalance: false
    clonefrom: false
    nosync: false

```

```
scope: pgsql
namespace: /service/
name: pg2

restapi:
  listen: 0.0.0.0:8008
  connect_address: 192.168.33.11:8008

zookeeper:
    hosts: 192.168.33.10:2181,192.168.33.11:2181  # Zookeeper 集群地址

bootstrap:
  dcs:
    ttl: 30
    loop_wait: 10
    retry_timeout: 10
    maximum_lag_on_failover: 1048576
    master_start_timeout: 300
    synchronous_mode: true
    postgresql:
      use_pg_rewind: true
      use_slots: true
      parameters:
        listen_addresses: "0.0.0.0"
        port: 5432
        wal_level: logical
        hot_standby: "on"
        wal_keep_segments: 100
        max_wal_senders: 10
        max_replication_slots: 10
        wal_log_hints: "on"

  initdb:
  - encoding: UTF8
  - locale: C
  - lc-ctype: zh_CN.UTF-8
  - data-checksums

  pg_hba:
  - host replication repl 0.0.0.0/0 md5
  - host all all 0.0.0.0/0 md5

postgresql:
  listen: 0.0.0.0:5432
  connect_address: 192.168.33.11:5432
  data_dir: /var/lib/pgsql/13/data
  bin_dir: /usr/pgsql-13/bin

  authentication:
    replication:
      username: repl
      password: "123456"
    superuser:
      username: postgres
      password: "123456"

  basebackup:
    max-rate: 100M
    checkpoint: fast

tags:
    nofailover: false
    noloadbalance: false
    clonefrom: false
    nosync: false
```




/etc/systemd/system/patroni.service

```
[Unit]
Description=Runners to orchestrate a high-availability PostgreSQL
After=syslog.target network.target
 
[Service]
Type=simple
User=postgres
Group=postgres
#StandardOutput=syslog
ExecStart=/usr/local/bin/patroni /etc/patroni.yml
ExecReload=/bin/kill -s HUP $MAINPID
KillMode=process
TimeoutSec=30
Restart=no
 
[Install]
WantedBy=multi-user.target
```

yum install keepalived

### keepalived.conf

```
vrrp_script chk_patroni {
    script "curl -s http://localhost:8008/health | grep '\"state\": \"running\"'"
    interval 2
    weight -2
}

vrrp_instance VI_1 {
    state MASTER
    interface eth1  # 替换为你的网络接口名
    virtual_router_id 51
    priority 100  # 主节点优先级较高
    advert_int 1

    authentication {
        auth_type PASS
        auth_pass 1234
    }

    virtual_ipaddress {
        192.168.33.100  # 虚拟 IP 地址
    }

    track_script {
        chk_patroni  # 关联 Patroni 健康检查脚本
    }
}

```

systemctl start keepalived.service