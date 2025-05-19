* core-site.xml

```
<configuration>
 <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
</configuration>
```

* hdfs-site.xml

```
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
    <property>
        <name>dfs.permissions</name>
        <value>false</value>
    </property>
           <property>
        <name>dfs.namenode.name.dir</name>
        <value>/data/disk_01/hdfs/name</value>
    </property>
    <property>
        <name>dfs.datanode.data.dir</name>
        <value>/data/disk_01/hdfs/data</value>
    </property>
</configuration>

```

* 验证服务
  
```
bin/hadoop
```

* 格式化

```
bin/hdfs namenode -format
```