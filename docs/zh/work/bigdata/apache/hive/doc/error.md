* FAILED: SemanticException org.apache.hadoop.hive.ql.metadata.HiveException: java.lang.RuntimeException: Unable to instantiate org.apache.hadoop.hive.ql.metadata.SessionHiveMetaStoreClient

hive2.x版本需要启动两个服务metastore和hiveserver2

```
nohup bin/hive --service metastore &
nohup bin/hive --service hiveserver2 &

```

* Caused by: MetaException(message:Version information not found in metastore. )

```
rm -rf metasotre_db
bin/schematool -dbType derby -initSchema
```

* Relative path in absolute URI: ${system:java.io.tmpdir%7D/$%7Bsystem:user.name%7D

```
sed -i 's/\${system:java\.io\.tmpdir}/\/tmp/g; s/\${system:user\.name}/root/g' conf/hive-site.xml
```

* FAILED: SemanticException org.apache.hadoop.hive.ql.metadata.HiveException: java.lang.RuntimeException: Unable to instantiate org.apache.hadoop.hive.ql.metadata.SessionHiveMetaStoreClient

```
  <property>
    <name>hive.metastore.uris</name>
    <value>thrift://localhost:9083</value>
    <description>Thrift URI for the remote metastore. Used by metastore client to connect to remote metastore.</description>
  </property>

```

*  User: root is not allowed to impersonate anonymous (state=08S01,code=0)
core-site.xml
```
<property>
	<name>hadoop.proxyuser.root.hosts</name>
	<value>*</value>
</property>
<property>
	<name>hadoop.proxyuser.root.groups</name>
	<value>*</value>
</property>
```



 * Establishing SSL connection without server's identity verification is not recommended. According to MySQL 5.5.45+, 5.6.26+ and 5.7.6+ requirements SSL connection must be established by default if explicit option isn't set. For compliance with existing applications not using SSL the verifyServerCertificate property is set to 'false'. You need either to explicitly disable SSL by setting useSSL=false, or set useSSL=true and provide truststore for server certificate verification.

        请注意:不建议在没有服务器身份验证的情况下建立SSL连接。根据MySQL 5.5.45+、5.6.26+和5.7.6+的要求，如果不设置显式选项，则必须建立默认的SSL连接。您需要通过设置useSSL=false显式地禁用SSL，或者设置useSSL=true并为服务器证书验证提供信任存储

        解决：

        设置useSSL=false
        这里有个坑就是hive的配置文件是.XML格式，而在xml文件中&amp；才表示&，所以正确的做法是在Hive的配置文件中，如hive-site.xml进行如下设置

        <property>
            <name>javax.jdo.option.ConnectionURL</name>
            <value>jdbc:mysql://localhost:3306/hive?createDatabaseIfNotExist=true&amp;useSSL=false</value>
            <description>JDBC connect string for a JDBC metastore</description>
        </property>
