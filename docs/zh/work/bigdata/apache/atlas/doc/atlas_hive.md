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