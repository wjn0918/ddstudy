* mapreduce_shuffle does not exist

```
<property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
  </property>
```


* httpfs 禁止代理

403 Client Error: Forbidden for url: http://localhost:14000/webhdfs/v1/user/admin?user.name=hue&doas=admin&op=GETFILESTATUS { "RemoteException" : { "message" : "User: hue is not allowed to impersonate admin", "exception" : "AuthorizationException", "javaClassName" : "org.apache.hadoop.security.authorize.AuthorizationException" } } (error 403)

需要同时配置core-site.xml, httpfs-site.xml


httpfs-site.xml
```
		<property>
                <name>httpfs.proxyuser.hue.hosts</name>
                <value>*</value>
        </property>

        <property>
                <name>httpfs.proxyuser.hue.groups</name>
                <value>*</value>
        </property>

```

core-site.xml
```
  	<property>
        <name>hadoop.proxyuser.hue.hosts</name>
        <value>*</value>
	</property>
	<property>
        <name>hadoop.proxyuser.hue.groups</name>
        <value>*</value>
	</property>

```