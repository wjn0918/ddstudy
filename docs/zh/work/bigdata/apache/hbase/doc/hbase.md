复制core-site.xml hdfs-site.xml

hbase-env.sh
```
# 不使用自带zookeeper
export HBASE_MANAGES_ZK=false




#Java安装目录，建议使用JDK 1.8：
export JAVA_HOME=<<JDK install path>>
export HADOOP_HOME=/home/hadoop/hadoop-2.10.1
export HBASE_HOME=/home/hadoop/hbase-2.4.9
export HADOOP_CONF_DIR=${HADOOP_HOME}/etc/hadoop
#配置HBase HMaster进程运行堆内存为16GB
export HBASE_MASTER_OPTS="-Xmx16384m"
#配置HBase分区服务器进程运行JVM参数，读者需要根据节点内存做调整，关于JVM调优可见第9章
export HBASE_REGIONSERVER_OPTS="-Xss256k -Xmx24g -Xms24g –Xmn2g 
-XX:MaxDirectMemorySize=24g -XX:SurvivorRatio=3 -XX:+UseParNewGC 
-XX:+UseConcMarkSweepGC -XX:MaxTenuringThreshold=10  
-XX:CMSInitiatingOccupancyFraction=80 -XX:+UseCMSCompactAt FullCollection
-XX:+UseCMSInitiatingOccupancyOnly 
-XX:+DisableExplicitGC -XX:+He apDumpOnOutOfMemoryError
-verbose:gc -XX:+PrintGCDateStamps -XX:+PrintGCTimeStamps -XX:+PrintGCDetails 
-XX:+PrintTenuringDistribution -XX:+PrintCommandLineFlags
-XX:ErrorFile=${HBASE_HOME}/logs/hs_err_pid%p-$(hostname).log
-XX:HeapDumpPath=${HBASE_HOME}/logs/ 
-Xloggc:${HBASE_HOME}/logs/gc-$(hostname)-hbase.log"
export HBASE_SSH_OPTS="-p 16120"
export HBASE_LOG_DIR=${HBASE_HOME}/logs
export HBASE_PID_DIR=${HBASE_HOME}/pid
export HBASE_MANAGES_ZK=false
#配置HBase运行相关的依赖库地址
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${HADOOP_HOME}/lib/native/:/usr/local/lib/
export HBASE_LIBRARY_PATH=${HBASE_LIBRARY_PATH}:${HBASE_HOME}/lib/native/Linux-
amd64-64:/usr/local/lib/:${HADOOP_HOME}/lib/native/

```

分布式配置 将hdfs-site.xml 复制到hbase中
```
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
    <property>
        <name>hbase.rootdir</name>
        <value>hdfs://mtcluster/user/hbase</value>
    </property>
    <property>
        <name>zookeeper.znode.parent</name>
        <value>/hbase</value>
    </property>
    <property>
        <name>hbase.cluster.distributed</name>
        <value>true</value>
    </property>
    <property>
        <name>hbase.tmp.dir</name>
        <value>/home/hadoop/data01/hbase/hbase_tmp</value>
    </property>
    <property>
        <name>hbase.zookeeper.property.dataDir</name>
        <value>/home/hadoop/data01/hbase/zookeeper_data</value>
    </property>
    <property>
        <name>hbase.master.port</name>
        <value>61000</value>
    </property>
    <property>
        <name>hbase.zookeeper.quorum</name>
        <value>master1,master2,slave1</value>
    </property>
    <property>
        <name>hbase.zookeeper.property.clientPort</name>
        <value>2181</value>
     </property>
    <property>
        <name>hbase.client.keyvalue.maxsize</name>
        <value>0</value>
    </property>
    <property>
        <name>hbase.master.distributed.log.splitting</name>
        <value>true</value>
    </property>
     <!--一次RPC请求读取的数据行数，设置该参数有助于优化读取效率，详细介绍可见9.1.2节 -->
    <property>
        <name>hbase.client.scanner.caching</name>
        <value>500</value>
    </property>
    <property>
        <name>hfile.block.cache.size</name>
        <value>0.2</value>
    </property>
    <!--当分区中存储文件的大小超过该值时，该分区可能会被拆分（受是否开启了自动拆分影响），一般线上集群会关闭自动拆分以免影响性能，因此会将该值设置得比较大，如100GB-->
    <property>
        <name>hbase.hregion.max.filesize</name>
        <value>107374182400</value><!-- 100GB -->
    </property>
    <property>
        <name>hbase.hregion.memstore.flush.size</name>
        <value>268435456</value><!-- 256MB -->
    </property>
    <property>
        <name>hbase.regionserver.handler.count</name>
        <value>200</value>
    </property>
    <property>
        <name>hbase.regionserver.global.memstore.lowerLimit</name>
        <value>0.38</value>
    </property>
    <property>
        <name>hbase.regionserver.global.memstore.size</name>
        <value>0.45</value>
    </property>
    <property>
        <name>hbase.hregion.memstore.block.multiplier</name>
        <value>8</value>
    </property>
    <property>
        <name>hbase.server.thread.wakefrequency</name>
        <value>1000</value>
    </property>
    <property>
        <name>hbase.rpc.timeout</name>
        <value>400000</value>
    </property>
    <!--当HStore的存储文件的数量超过该值时，MemStore刷新到磁盘之前需要进行拆分或者合并，除非超过hbase.hstore.blockingWaitTime配置的时间。因此，当禁止自动大合并时该配置项一定要配置一个较大的值-->
    <property>
        <name>hbase.hstore.blockingStoreFiles</name>
        <value>5000</value>
    </property>
    <property>
        <name>hbase.client.scanner.timeout.period</name>
        <value>1000000</value>
    </property>
    <property>
        <name>zookeeper.session.timeout</name>
        <value>180000</value>
    </property>
    <property>
        <name>hbase.regionserver.optionallogflushinterval</name>
        <value>5000</value>
    </property>
        <property>
        <name>hbase.client.write.buffer</name>
        <value>5242880</value>
    </property>
    <!--当HStore的存储文件的数量超过该值时，可能会触发合并，该值不能设置得过大，否则会影响读性能，一般建议设置为3~5-->
    <property>
        <name>hbase.hstore.compactionThreshold</name>
        <value>5</value>
    </property>
    <property>
        <name>hbase.hstore.compaction.max</name>
        <value>12</value>
    </property>
    <!--将该值设置为1以禁止线上表的自动拆分，可以在创建表的时候预分区或者之后手动分区-->
    <property>
        <name>hbase.regionserver.regionSplitLimit</name>
        <value>1</value>
    </property>
    <property>
        <name>hbase.regionserver.thread.compaction.large</name>
        <value>5</value>
    </property>
    <property>
        <name>hbase.regionserver.thread.compaction.small </name>
        <value>8</value>
    </property>
    <property>
        <name>hbase.master.logcleaner.ttl</name>
        <value>3600000</value>
    </property>
    <property>
        <name>hbase.bucketcache.ioengine</name>
        <value>offheap</value>
    </property>
    <property>
        <name>hbase.bucketcache.percentage.in.combinedcache</name>
        <value>0.9</value>
    </property>
    <!--BucketCache 的大小  16G-->
    <property>
        <name>hbase.bucketcache.size</name>
        <value>16384</value>
    </property>
    <property>
        <name>hbase.replication</name>
        <value>true</value>
    </property>
     <!--开启镜像(snapshot)功能支持-->
    <property>
        <name>hbase.snapshot.enabled</name>
        <value>true</value>
    </property>
    <!--复制带宽限制：默认为0表示不限速，如果复制带宽限速100MB，就填写100*1024*1024 =  
104857600-->
    <property>
        <name>replication.source.per.peer.node.bandwidth</name>
        <value>104857600</value>
    </property>
    <!--复制主集群能够选择从集群的服务器百分比，如果从集群有3台机器，则配置值1表示主集群能够选择所有的3台机器用来推送复制数据-->
    <property>
         <name>replication.source.ratio</name>
         <value>1</value>
    </property>
    <!--配置大合并的间隔时间，0表示禁止自动大合并，如果是线上响应时间敏感的应用，则建议禁止而等到非高峰期手动合并，否则很有可能导致HBase响应超时而引起性能抖动-->
    <property>
         <name>hbase.hregion.majorcompaction</name>
         <value>0</value>
    </property>
</configuration>

```


# hbase ddl

create 'tabel_name' 'column_family_name'