# idea new scala

需要添加scala编译插件

```
<plugin>
    <groupId>net.alchim31.maven</groupId>
    <artifactId>scala-maven-plugin</artifactId>
    <version>3.1.4</version>
    <executions>
        <execution>
            <id>scala-compile-first</id>
            <phase>process-resources</phase>
            <goals>
                <goal>add-source</goal>
                <goal>compile</goal>
            </goals>
        </execution>
        <execution>
            <id>scala-test-compile</id>
            <phase>process-test-resources</phase>
            <goals>
                <goal>testCompile</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```


* 空对象

```
var confInstance: String = _

```

* 允许空值case class

```
case class Org2(
                 orgIndexCode: String,
                 organizationCode: Option[String],
                 orgName: String,
                 orgPath: String,
                 parentOrgIndexCode: String,
                 available: Boolean,
                 leaf: Boolean,
                 sort: Number,
                 createTime: Option[String],
                 updateTime: String
               )
```

* 泛型传递

```
  def getData[A]()(implicit mf: scala.reflect.Manifest[A]): List[A] = {
    if (ETLConfig.dataSource == "api") {
      getDataFromApi[A]()(mf)
    } else {
      getDataFromLocal[A]()(mf)
    }
  }


private def getDataFromLocal[A]()(implicit mf: scala.reflect.Manifest[A]): List[A] = {
    val r = scala.io.Source.fromFile(this.filePath).mkString
    pareJson[A](r)
  }

```