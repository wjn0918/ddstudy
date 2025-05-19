# 强类型转换

spark-defaults.conf

spark.sql.storeAssignmentPolicy=LEGACY


# 配置python解析器
https://spark.apache.org/docs/latest/configuration.html
spark.pyspark.python


# udf 返回数组

```
// 定义正则表达式
val myPattern: Regex = "([0-9]*)([^0-9]*)(.*)".r

def getOrgInfo = udf((orgName: String) =>
  orgName match {
    case myPattern(year, major, classNum) => Seq(year, major, classNum)
    case _ => Seq(null, null, null)
  }
)
spark.udf.register("get_org_info", getOrgInfo)


//spark.sql("select get_org_info(a)[0] from  (select '2013建筑工程管理4班' as a)").show()
```


# spark on yarn 

```
# spark-env.sh

export SPARK_HOME=$SPARK_HOME
export JAVA_HOME=$JAVA_HOME
export HADOOP_HOME=$HADOOP_HOME
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export YARN_CONF_DIR=$HADOOP_HOME/etc/hadoop
export SPARK_LOCAL_DIRS=$SPARK_HOME
```


* spark on yarn 查看结束APPLICATION的执行情况

spark-defaults.conf

不生效需要删除原本的配置文件

```
spark.master                     yarn
#开启事件日志
spark.eventLog.enabled           true
#这里是日志的存放路径，需要与该代码块中的最后一项保持一致
spark.eventLog.dir               hdfs://192.168.3.204:9000/user/spark/log
#这一句是访问历史任务日志的地址
spark.yarn.historyServer.address 192.168.3.204:18080
#压缩
spark.eventLog.compress          true
#与第三项保持一致
spark.history.fs.logDirectory    hdfs://192.168.3.204:9000/user/spark/log
```

spark-env.sh

```
#端口号18080与上面文件配置确保一致，retainedApplications表示保留历史任务的个数。路径与上面配置保持一致
export SPARK_HISTORY_OPTS="-Dspark.history.ui.port=18080 -Dspark.history.retainedApplications=7 -Dspark.history.fs.logDirectory=hdfs://192.168.3.204:9000/user/spark/log"

```


sbin/start-history-server.sh


* 设置日志级别

Logger.getLogger("org.apache.spark").setLevel(Level.ERROR)

使用自定义log4j

```

import org.apache.log4j.{Level, Logger, PropertyConfigurator}
import org.apache.spark.sql.SparkSession

object Log4jTest {



  def main(args: Array[String]): Unit = {

    PropertyConfigurator.configure(Log4jTest.getClass.getResource("/log4j.properties"))
    Logger.getLogger("org.apache.spark").setLevel(Level.WARN)

    val logger = Logger.getLogger(Log4jTest.getClass)
    val spark = SparkSession.builder().appName("demo").getOrCreate()

    import spark.implicits._
    val value = spark.createDataset(Seq(1, 2))
    value.show()


    logger.info("1231")
  }

}
```


* idea 设置master

vm options  -Dspark.master=local[4]

# 提交作业

spark-submit --master local[4] --class cn.shingi.schooletl.spark.batch.SchoolETLSparkBatch jar