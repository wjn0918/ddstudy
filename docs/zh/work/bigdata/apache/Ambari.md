---
title: Ambari
---


[自定义stack](https://cwiki.apache.org/confluence/display/AMBARI/How-To+Define+Stacks+and+Services)

https://www.yuque.com/create17/ambari/pqrb9q#tsdHa


http://192.168.3.13:8080/#/installer/step0




## centos 编译

maven == 3.6.3
node == 10.9.0
git
bower
gcc-c++
python-devel



JDK选择1.8
node选择10(6也行)
提前下载好phantomjs-1.9.7-linux-x86_64.tar.bz2包,最好同时下载1.9.8和2.1.1版本(因为你也没办法确认最终会使用哪个),将它们放在==/tmp/phantomjs==路径下,这一步非常重要,这是前端依赖包,这样做可以避免因为没有办法科学冲浪导致的打包失败.





ambari-web更改pom.xml

```
<plugin>
    <groupId>com.github.eirslett</groupId>
    <artifactId>frontend-maven-plugin</artifactId>
    <version>1.4</version>
    <configuration>
        <nodeVersion>v4.5.0</nodeVersion>
        <yarnVersion>v0.23.2</yarnVersion>
        <workingDirectory>${basedir}</workingDirectory>
        <npmInheritsProxyConfigFromMaven>false</npmInheritsProxyConfigFromMaven>
        <!-- setting npm_config_tmp environment variable is a workaround for
                https://github.com/Medium/phantomjs/issues/673 -->
                    <!-- 若不方便访问官网，可使用国内淘宝镜像-->
        <nodeDownloadRoot>https://npm.taobao.org/mirrors/node/</nodeDownloadRoot>
        <npmDownloadRoot>https://registry.npm.taobao.org/npm/-/</npmDownloadRoot>
        <environmentVariables>
            <npm_config_tmp>/tmp/npm_config_tmp</npm_config_tmp>
        </environmentVariables>
    </configuration>
    <executions>
        <execution>
            <id>install node and yarn</id>
            <phase>generate-sources</phase>
            <goals>
                <goal>install-node-and-yarn</goal>
            </goals>
        </execution>
        <execution>
            <id>yarn install</id>
            <phase>generate-sources</phase>
            <goals>
                <goal>yarn</goal>
            </goals>
            <configuration>
                <arguments>install --ignore-engines --pure-lockfile</arguments>
            </configuration>
        </execution>
    </executions>
</plugin>

```


ambari-metrics

添加依赖
下载storm-core-0.10.0.2.3.0.0-2557.jar 并指定本地路径
https://mvnrepository.com/artifact/org.apache.storm/storm-core/0.10.0.2.3.0.0-2557
```
<dependency>
      <groupId>org.apache.storm</groupId>
      <artifactId>storm-core</artifactId>
      <version>${storm.version}</version>
      <systemPath>/root/storm-core-0.10.0.2.3.0.0-2557.jar</systemPath>
      <scope>system</scope>
    </dependency>
<dependency>
     <groupId>com.googlecode.json-simple</groupId>
     <artifactId>json-simple</artifactId>
     <version>1.1</version>
</dependency>
```

ambari-metrics-timelineservice

```
zookeeper 版本改为3.4.5
```



## 更改ambari-metrics pom




<hbase.tar>file:///root/hbase-2.4.2-bin.tar.gz</hbase.tar>
<hadoop.tar>file:///root/hadoop-3.1.1.tar.gz</hadoop.tar>
<grafana.tar>file:///root/grafana-6.7.4.linux-amd64.tar.gz</grafana.tar>
<phoenix.tar>file:///root/phoenix-hbase-2.4-5.1.2-bin.tar.gz</phoenix.tar>

https://dl.grafana.com/oss/release/grafana-6.7.4.linux-amd64.tar.gz
https://archive.apache.org/dist/hadoop/common/hadoop-3.1.1/hadoop-3.1.1.tar.gz
https://downloads.apache.org/phoenix/phoenix-5.1.2/phoenix-hbase-2.4-5.1.2-bin.tar.gz






ambari-logsearch

zookeeper版本改为3.4.6


## ambari-logsearch-it


添加
```
  <repositories> 
        <repository> 
            <id>maven-restlet</id> 
            <name>Public online Restlet repository</name> 
            <url>http://maven.restlet.org</url> 
        </repository> 
    </repositories> 
```

## ambari-infra 

zookeeper 版本更改3.4.6



```
echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p

# 安装phantomjs
https://phantomjs.org


ln -s /usr/local/phantomjs/bin/phantomjs /usr/local/bin/phantomjs
```


```
mvn versions:set -DnewVersion=2.7.7.0.0
pushd ambari-metrics
mvn versions:set -DnewVersion=2.7.7.0.0
popd

sudo yum install rpm-build

mvn -B clean install rpm:rpm -DnewVersion=2.7.7.0.0 -DbuildNumber=388e072381e71c7755673b7743531c03a4d61be8 -DskipTests -Dpython.ver="python >= 2.6"
```



## 安装


cd /root/apache-ambari-2.7.7-src/ambari-server/target/rpm/ambari-server/RPMS/x86_64


yum install *.rpm

ambari-server setup
ambari-server start

admin/admin