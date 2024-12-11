---
title: Atlas
---


## 编译atlas


mvn clean -DskipTests install

mvn clean -DskipTests package -Pdist,embedded-hbase-solr

## 启动zookeeper


## 启动hbase


## 启动solr

solr/bin/solr start -p 8983 -z localhost:2181 -force


## 创建索引

solr/bin/solr  create -c fulltext_index -force -d conf/solr/ 
solr/bin/solr  create -c edge_index -force -d conf/solr/   
solr/bin/solr  create -c vertex_index -force -d conf/solr/




First of all, executing the import-hive.sh command will only import Hive entities (DBs, tables, columns) into Atlas. It won't create the inter-table lineage.

# 导入hive元数据




# 实时加载hive元数据
```
# vim hive-site.xml

<property>
      <name>hive.exec.post.hooks</name>
      <value>org.apache.atlas.hive.hook.HiveHook</value>
</property>
<property>
      <name>hive.reloadable.aux.jars.path</name>
      <value>/usr/local/atlas/hook/hive</value>
</property>


# hive-env.sh
export HIVE_AUX_JARS_PATH=/usr/local/atlas/hook/hive

# 重启hiveserver2 和hive metastore


```



# 无法实时加载hive元数据

* 查看hive配置文件中相关配置是否冲突了






```
[root@ipaserver bin]# python atlas_start.py 
Exception: [Errno 2] No such file or directory 
Traceback (most recent call last):
  File "atlas_start.py", line 163, in <module>
    returncode = main()
  File "atlas_start.py", line 73, in main
    mc.expandWebApp(atlas_home)
  File "/root/apache-atlas-sources-2.1.0/distro/target/apache-atlas-2.1.0-server/apache-atlas-2.1.0/bin/atlas_config.py", line 162, in expandWebApp
    jar(atlasWarPath)
  File "/root/apache-atlas-sources-2.1.0/distro/target/apache-atlas-2.1.0-server/apache-atlas-2.1.0/bin/atlas_config.py", line 215, in jar
    process = runProcess(commandline)
  File "/root/apache-atlas-sources-2.1.0/distro/target/apache-atlas-2.1.0-server/apache-atlas-2.1.0/bin/atlas_config.py", line 251, in runProcess
    p = subprocess.Popen(commandline, stdout=stdoutFile, stderr=stderrFile, shell=shell)
  File "/usr/lib64/python2.7/subprocess.py", line 711, in __init__
    errread, errwrite)
  File "/usr/lib64/python2.7/subprocess.py", line 1327, in _execute_child
    raise child_exception
OSError: [Errno 2] No such file or directory




# JAVA_HOME指向jre ，所以bin 下面没有jar 这个工具

export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.372.b07-1.el7_9.x86_64

```


# 创建索引节点

solr/bin/solr  create -c fulltext_index -force -d conf/solr/ 
solr/bin/solr  create -c edge_index -force -d conf/solr/   
solr/bin/solr  create -c vertex_index -force -d conf/solr/




# atlas_hive

* Caused by: org.apache.commons.configuration.ConversionException: 'atlas.graph.index.search.solr.wait-searcher' doesn't map to a List object: true, a java.lang.Boolean

将/atlas/hook/hive/atlas-hive-plugin-impl/commons-configuration-1.10.jar复制到/usr/local/hive/lib目录下

* Exception in thread "main" java.lang.NoSuchMethodError: org.apache.hadoop.hive.metastore.api.Database.getCatalogName()Ljava/lang/String;


Atlas 代码中用的 Hive 版本为3.1.0
修改addons/hive-bridge/src/main/java/org/apache/atlas/hive/bridge/HiveMetaStoreBridge.java 
getDatabaseName

```
public static String getDatabaseName(Database hiveDB) {
    String dbName      = hiveDB.getName().toLowerCase();
    /*
    String catalogName = hiveDB.getCatalogName() != null ? hiveDB.getCatalogName().toLowerCase() : null;

    if (StringUtils.isNotEmpty(catalogName) && !StringUtils.equals(catalogName, DEFAULT_METASTORE_CATALOG)) {
        dbName = catalogName + SEP + dbName;
    }
    */

    return dbName;
}
```


这个新的包替换atlas-hive-plugin-impl目录下的文件