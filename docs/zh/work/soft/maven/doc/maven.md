# 跳过编译成功的module
```
格式：
mvn <goals> -rf :<moduleName>

说明：
goals: 就是mvn命令后的内容
moduleName：指定从哪个模块开始继续执行goals。

基于我的情况，例子如下：
mvn clean install -DskipTests=false -rf :moduleName

-rf :ambari-metrics-host-monitoring
```



export MAVEN_OPTS="-Xms2g -Xmx2g"



# 下载文件
```
<profile>
            <id>embedded-hbase-solr</id>
            <activation>
                <activeByDefault>false</activeByDefault>
            </activation>
            <properties>
                <graph.storage.properties>#Hbase
#For standalone mode , specify localhost
#for distributed mode, specify zookeeper quorum here
atlas.graph.storage.hostname=localhost
atlas.graph.storage.hbase.regions-per-server=1
atlas.graph.storage.lock.wait-time=10000
                </graph.storage.properties>
                <graph.index.properties>#Solr
#Solr cloud mode properties
atlas.graph.index.search.solr.mode=cloud
atlas.graph.index.search.solr.zookeeper-url=localhost:2181
atlas.graph.index.search.solr.zookeeper-connect-timeout=60000
atlas.graph.index.search.solr.zookeeper-session-timeout=60000
atlas.graph.index.search.solr.wait-searcher=true

#Solr http mode properties
#atlas.graph.index.search.solr.mode=http
#atlas.graph.index.search.solr.http-urls=http://localhost:8983/solr
                </graph.index.properties>

                <cassandra.embedded>false</cassandra.embedded>
                <hbase.embedded>true</hbase.embedded>
                <solr.embedded>true</solr.embedded>

                <hbase.dir>${project.build.directory}/hbase</hbase.dir>
                <hbase.tar>https://archive.apache.org/dist/hbase/${hbase.version}/hbase-${hbase.version}-bin.tar.gz</hbase.tar>
                <hbase.folder>hbase-${hbase.version}</hbase.folder>

                <solr.dir>${project.build.directory}/solr</solr.dir>
                <solr.tar>https://archive.apache.org/dist/lucene/solr/${solr.version}/solr-${solr.version}.tgz</solr.tar>
                <solr.folder>solr-${solr.version}</solr.folder>
            </properties>
            <build>
                <plugins>
                    <plugin>
                        <groupId>org.apache.maven.plugins</groupId>
                        <artifactId>maven-antrun-plugin</artifactId>
                        <version>1.7</version>
                        <executions>
                            <!-- package hbase -->
                            <execution>
                                <id>hbase</id>
                                <phase>generate-resources</phase>
                                <goals>
                                    <goal>run</goal>
                                </goals>
                                <configuration>
                                    <target name="Download HBase">
                                        <!-- <mkdir dir="${hbase.dir}" />
                                        <mkdir dir="${project.basedir}/hbase" />
                                        <get src="${hbase.tar}" dest="${project.basedir}/hbase/${hbase.folder}.tar.gz" usetimestamp="true" verbose="true" skipexisting="true" /> -->
                                        <untar src="${project.basedir}/hbase/${hbase.folder}.tar.gz" dest="${project.build.directory}/hbase.temp" compression="gzip" />
                                        <copy todir="${hbase.dir}">
                                            <fileset dir="${project.build.directory}/hbase.temp/${hbase.folder}">
                                                <include name="**/*" />
                                            </fileset>
                                        </copy>
                                    </target>
                                </configuration>
                            </execution>
                            <!-- package solr -->
                            <execution>
                                <id>solr</id>
                                <phase>generate-resources</phase>
                                <goals>
                                    <goal>run</goal>
                                </goals>
                                <configuration>
                                    <target name="Download SOLR">
                                        <!-- <mkdir dir="${solr.dir}" />
                                        <mkdir dir="${project.basedir}/solr" />
                                        <get src="${solr.tar}" dest="${project.basedir}/solr/${solr.folder}.tgz" usetimestamp="true" verbose="true" skipexisting="true" /> -->
                                        <untar src="${project.basedir}/solr/${solr.folder}.tgz" dest="${project.build.directory}/solr.temp" compression="gzip" />
                                        <copy todir="${solr.dir}">
                                            <fileset dir="${project.build.directory}/solr.temp/${solr.folder}">
                                                <include name="**/*" />
                                            </fileset>
                                        </copy>
                                    </target>
                                </configuration>
                            </execution>
                        </executions>
                    </plugin>
                </plugins>
            </build>
        </profile>
```



# maven 仓库


```
<mirror>
    <id>centralhttps</id>
    <mirrorOf>central</mirrorOf>
    <name>Maven central https</name>
    <url>http://insecure.repo1.maven.org/maven2/</url>
</mirror>
</mirrors>
```