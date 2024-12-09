# [使用keepalived](https://www.cnblogs.com/wenxuehai/p/15013654.html)




# 使用zookeeper
```
from kazoo.client import KazooClient
from kazoo.recipe.election import Election
import os
import time

zk = KazooClient(hosts='192.168.1.1:2181,192.168.1.2:2181')  # Zookeeper 集群地址
zk.start()

election = Election(zk, "/nginx-master")

def run_as_master():
    print("I am the leader now, starting Nginx...")
    os.system("systemctl start nginx")
    while True:
        time.sleep(5)  # 保持主节点状态

def stop_nginx():
    print("I am not the leader, stopping Nginx...")
    os.system("systemctl stop nginx")

@zk.DataWatch("/nginx-master")
def watch_node(data, stat):
    if stat and data:
        print("Another leader is active.")
        stop_nginx()

# 参与选举
election.run(run_as_master)


```