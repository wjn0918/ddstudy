* Spark hive udf: no handler for UDAF analysis exception

需要配置

spark.sql.catalogImplementation  hive


# tinyint 的0 被转为 true
jdbc 设置
&tinyInt1isBit=false


* User did not initialize spark context!


代码中是否包含了setmaster,有的话注释掉


* spark-submit报错Exception in thread “main“ java.sql.SQLException: No suitable driver found

jdk1.8.0_171/jre/lib/ext mysql驱动包放到这里


* Caused by: java.io.NotSerializableException: net.liftweb.json.DefaultFormats$

这个错误是因为DefaultFormats类没有被序列化，而在Spark的分布式计算环境中，函数需要被序列化以便在集群中传输。为了解决这个问题，你可以将DefaultFormats对象传递给你的Spark任务，但要确保它是transient（瞬态）的，以避免序列化。然后在Spark任务中重新创建DefaultFormats。

这里是一个示例：

scala
Copy code
class YourSparkJob {
  @transient implicit val customFormats: Formats = DefaultFormats

  // 在你的 Spark 任务中使用 customFormats
  def yourSparkTask(): Unit = {
    implicit val customFormats: Formats = DefaultFormats
    // ...
  }
}