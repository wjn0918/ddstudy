```
import org.apache.flink.streaming.api.scala._
import org.apache.flink.table.api._
import org.apache.flink.table.api.bridge.scala._

object CsDemo {


  def main(args: Array[String]): Unit = {
    val env = StreamExecutionEnvironment.getExecutionEnvironment
    val settings = EnvironmentSettings.newInstance().useBlinkPlanner().inStreamingMode().build()
    val tableEnv = StreamTableEnvironment.create(env, settings)

    val sourceDDL =
      """
        |CREATE TABLE t_cs (
        |  name string
        |) WITH (
        |  'connector' = 'mysql-cdc',
        |  'hostname' = 'localhost',
        |  'port' = '3307',
        |  'username' = 'root',
        |  'password' = '123456',
        |  'database-name' = 'cs',
        |  'table-name' = 't_cs',
        |  'scan.incremental.snapshot.enabled' = 'false'
        |)
        |""".stripMargin

    val sinkDDL =
      """
        |CREATE TABLE t_cs_copy (
        |  name string,
        |  PRIMARY KEY (name) NOT ENFORCED
        |) WITH (
        |  'connector' = 'jdbc',
        |  'url' = 'jdbc:mysql://localhost:3307/cs',
        |  'username' = 'root',
        |  'password' = '123456',
        |  'table-name' = 't_cs_copy'
        |)
        |""".stripMargin

    val query =
      """
        |INSERT INTO t_cs_copy
        |SELECT * FROM t_cs
        |""".stripMargin

    tableEnv.executeSql(sourceDDL)
    tableEnv.executeSql(sinkDDL)

    tableEnv.executeSql(query)

  }
}


```