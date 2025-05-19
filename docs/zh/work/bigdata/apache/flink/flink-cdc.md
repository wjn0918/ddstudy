---
tilte: flink-cdc
---


```
   <dependencies>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-streaming-java</artifactId>
            <version>1.19.0</version>
        </dependency>

        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-clients</artifactId>
            <version>1.19.0</version>
        </dependency>

            <dependency>
                <groupId>org.apache.flink</groupId>
                <artifactId>flink-connector-base</artifactId>
                <version>1.19.0</version>
            </dependency>


        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-connector-postgres-cdc</artifactId>
            <version>3.1.0</version>
        </dependency>
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>fastjson</artifactId>
            <version>1.2.49</version>
        </dependency>
    </dependencies>

```

```

package org.example.hello.flinkcdc;

import org.apache.flink.cdc.connectors.postgres.PostgreSQLSource;
import org.apache.flink.cdc.debezium.JsonDebeziumDeserializationSchema;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.api.functions.source.SourceFunction;


public class HelloFlinkCdc  {
    //功能：测试实时读取pgsql数据
    public static void main(String[] args) throws Exception {
        SourceFunction<String> sourceFunction = PostgreSQLSource.<String>builder()
                .hostname("localhost")
                .port(5432)
                .database("test_db") // monitor postgres database
                .schemaList("public")  // monitor inventory schema
                .tableList("public.t_user") // monitor products table
                .username("postgres")
                .password("Pgsql@2024")
                .slotName("flink")
                .decodingPluginName("pgoutput") // use pgoutput for PostgreSQL 10+
                .deserializer(new JsonDebeziumDeserializationSchema()) // converts SourceRecord to JSON String
                .build();

        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

        env
                .addSource(sourceFunction)
                .print().setParallelism(1); // use parallelism 1 for sink to keep message ordering

        env.execute();
    }
}

```