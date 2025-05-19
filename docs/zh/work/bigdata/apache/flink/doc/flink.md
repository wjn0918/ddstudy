# 自定义source

```

%flink

import org.apache.flink.streaming.api.scala._
import org.apache.flink.streaming.api.functions.source.SourceFunction
import java.net.HttpURLConnection
import java.net.URL
import java.io.BufferedReader
import java.io.InputStreamReader
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter

class HttpSource() extends SourceFunction[String] {

    @volatile var isRunning = true

    override def run(ctx: SourceFunction.SourceContext[String]): Unit = {
      val dateFormat = DateTimeFormatter.ofPattern("yyyy-MM-dd'T'HH:mm:ss")

      while (isRunning) {
        val endTime = LocalDateTime.now()
        val startTime = endTime.minusSeconds(1)  // 假设每次查询最近1s的数据
        
        val formattedStartTime = startTime.format(dateFormat)
        val formattedEndTime = endTime.format(dateFormat)

        
        // 将数据收集到 Flink 流中
        ctx.collect(formattedStartTime.toString())

        // 每次调用间隔时间（如每1秒调用一次）
        Thread.sleep(1000)
      }
    }

    override def cancel(): Unit = {
      isRunning = false
    }
  }




%flink
val stream = senv.addSource(new HttpSource())
stream.print
senv.execute()

```



# 容灾

Savepoint（保存点）是用户手动触发的Checkpoint 常用于在升级和维护集群的过程中保存状态数据，避免系统无法恢复到原有的计算状态

# 类型擦除

* 显示指定类型
```
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        env.setRuntimeMode(RuntimeExecutionMode.BATCH);
        StreamTableEnvironment tabEnv = StreamTableEnvironment.create(env);
        FileSource<String> source = FileSource.forRecordStreamFormat(
                new TextLineInputFormat(),
                new Path("data/hello.txt")
        ).build();



        DataStreamSource<String> content = env.fromSource(source,
                WatermarkStrategy.noWatermarks(),
                "cs"
        );
         DataStream<Row> d1 = content.map(
                new MapFunction<String, Row>() {
                    @Override
                    public Row map(String value) throws Exception {

                        return Row.of(value.split(",")[0], "1");
                    }
                }
        ).returns(Types.ROW(Types.STRING,Types.STRING));
                Table table = tabEnv.fromDataStream(d1).as("name","age");
        tabEnv.createTemporaryView("t", table);
        tabEnv.executeSql("select * from t").print();

```



在Flink中，有两种连接器用于连接不同的数据源和数据接收器：DataStream Connector（数据流连接器）和DataSet Connector（数据集连接器）。它们之间的区别如下：

1. DataStream Connector（数据流连接器）：
   - 适用于实时流处理场景，处理连续的数据流。
   - 使用DataStream API进行编程。
   - 支持基于事件时间的窗口操作、流转换、状态管理等功能。
   - 通过数据流连接器，可以使用各种源（source）和接收器（sink）来读取和写入数据。例如，Kafka、RabbitMQ、Socket等。

2. DataSet Connector（数据集连接器）：
   - 适用于批处理场景，处理有限的数据集合。
   - 使用DataSet API进行编程。
   - 支持集合操作（如map、reduce、filter等）和关系型操作（如join、group by等）。
   - 通过数据集连接器，可以使用各种源（source）和接收器（sink）来读取和写入数据。例如，本地文件系统、HDFS、数据库等。

总结：
- DataStream Connector适用于实时流处理场景，使用DataStream API进行编程，支持流处理的特性和功能。
- DataSet Connector适用于批处理场景，使用DataSet API进行编程，支持批处理的特性和功能。
- 两者的主要区别在于处理的数据类型和编程模型，以及适用的场景。数据流连接器处理连续的数据流，适合实时处理；数据集连接器处理有限的数据集合，适合批处理。



# Table API


(1)连接外部系统。(2)注册catalog。(3)在内部catalog目录中注册一个Table。(4)从catalog目录中注册和检索Table和其他元对象。(5)提供进一步的配置选项。(6)执行SQL查询。(7)注册用户定义函数（标量函数、表函数或聚合函数）。(8)DataStream和Table之间的转换（在StreamTableEnvironment中）。