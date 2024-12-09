---
title: oozie
icon: lightbulb
---

bin/mkdistro.sh clean install -Dmaven.test.skip=true -DskipTests -Dmaven.wagon.http.ssl.insecure=true -Dhttp.connectionTimeout=60000 -Dhttp.socketTimeout=60000


https://oozie.apache.org/docs/5.2.1/DG_QuickStart.html#Building_Oozie


```
bin/oozie-setup.sh sharelib create -fs <FS_URI> [-locallib <PATH>]
                     sharelib upgrade -fs <FS_URI> [-locallib <PATH>]
                     db create|upgrade|postupgrade -run [-sqlfile <FILE>]


bin/oozie-setup.sh sharelib create -fs hdfs://node12:9000

bin/oozie admin -oozie http://localhost:11000/oozie -sharelibupdate
```




mkdir libext


find share -type f -name "*.jar" -exec cp {} libext/ \;
cp /tools/ext-2.2.zip /training/oozie-5.2.1/libext/


* java.lang.NoSuchMethodError: org.hsqldb.DatabaseURL.parseURL(Ljava/lang/String;ZZ)Lorg/hsqldb/persist/HsqlProperties

hsql jar冲突 改为低版本

* java.lang.NoClassDefFoundError: org/apache/hadoop/conf/Configuration

hadoop-common 复制到lib

* java.lang.NoClassDefFoundError: com/ctc/wstx/io/InputBootstrapper

cp libext/woodstox-core-5.4.0.jar lib