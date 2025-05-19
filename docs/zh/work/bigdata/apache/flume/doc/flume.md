bin/flume-ng agent --conf conf --conf-file example.conf --name a1


hbase-sink



```
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
  <property>
    <name>hbase.cluster.distributed</name>
    <value>true</value>
  </property>
  <property>
    <name>hbase.rootdir</name>
    <value>/hbase-data</value>
  </property>
  <property>
    <name>hbase.zookeeper.quorum</name>
    <value>192.168.3.210:2181</value>
  </property>
</configuration>
```