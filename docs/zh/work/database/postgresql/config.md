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

## 开启日志

```
vi postgresql.conf
```

### 配置
```
# 更改wal日志方式为logical（方式有：minimal、replica 、logical  ）
wal_level = logical  

# 更改solts最大数量（默认值为10），flink-cdc默认一张表占用一个slots
max_replication_slots = 20

# 更改wal发送最大进程数（默认值为10），这个值和上面的solts设置一样
max_wal_senders = 20     

# 中断那些停止活动超过指定毫秒数的复制连接，可以适当设置大一点（默认60s，0表示禁用）
wal_sender_timeout = 180s

```

```
SHOW wal_level;
```


### 更改密码

```
ALTER ROLE username WITH PASSWORD 'new_password';
```


### 创建用户

::: warning
用户名不要用大写
:::





```
-- pg新建用户
CREATE USER test1 WITH PASSWORD 'test123';

-- 给用户复制流权限
ALTER ROLE test1 replication;

-- 给用户数据库权限
GRANT CONNECT ON DATABASE test_db to test1;


```

### 发布表

- 设置发布开关

```
update pg_publication set puballtables=true where pubname is not null;

```
- 发布表

:::tabs

@tab 所有表

```
CREATE PUBLICATION dbz_publication FOR ALL TABLES;
```

@tab 单表


```
CREATE PUBLICATION publication_name FOR table table_name;
```

:::

- 查询哪些表已经发布

```
select * from pg_publication_tables;
```

```
-- 给表查询权限
grant select on TABLE aa to ODPS_ETL;

-- 给用户读写权限
grant select,insert,update,delete ON  ALL TABLES IN SCHEMA public to bd_test;

-- 把当前库所有表查询权限赋给用户
GRANT SELECT ON ALL TABLES IN SCHEMA public TO ODPS_ETL;

-- 把当前库以后新建的表查询权限赋给用户
alter default privileges in schema public grant select on tables to ODPS_ETL;

-- 更改复制标识包含更新和删除之前值
ALTER TABLE test0425 REPLICA IDENTITY FULL;

-- 查看复制标识
select relreplident from pg_class where relname='test0425';

-- 查看solt使用情况
SELECT * FROM pg_replication_slots;

-- 删除solt
SELECT pg_drop_replication_slot('zd_org_goods_solt');

-- 查询用户当前连接数
select usename, count(*) from pg_stat_activity group by usename order by count(*) desc;

-- 设置用户最大连接数
alter role odps_etl connection limit 200;

```