---
title: 使用
---

## gson使用泛型解析json
:::warning
使用 Java 的 List

Java 的类型擦除机制,正确地反序列化带有泛型参数的对象，你需要创建一个 TypeToken 来捕获完整的泛型类型信息

:::


```
case class Response[T](
                      code: String,
                      msg: String,
                      data: ResponseData[T]
                      )

case class ResponseData[T](
                      total: Int,
                      pageNo: Int,
                      pageSize: Int,
                      list: java.util.List[T]
                      )
                


Type type = new TypeToken<Response<FaceRecognitionResult>>(){}.getType();
Gson gson = new Gson();
Response r = gson.fromJson(content, type);

```




## idea 创建scala

添加scala-library 依赖

```
 <dependency>
    <groupId>org.scala-lang</groupId>
    <artifactId>scala-library</artifactId>
    <version>2.13.10</version>
</dependency>
```

需要添加scala编译插件

```
<build>
        <plugins>
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
        </plugins>
    </build>
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

