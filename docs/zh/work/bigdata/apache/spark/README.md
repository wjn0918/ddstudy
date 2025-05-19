---
title: Spark
---

## 更改ssh端口

spark-env.sh

export SPARK_SSH_OPTS="-p 7788"

## creating dataframe

- List\<Row>
```
List<Row> ids = new ArrayList<>();

StructType schema = new StructType(new StructField[]{
            DataTypes.createStructField("id", DataTypes.StringType, false),
    });
Dataset<Row> df = spark.createDataFrame(ids, schema);
```


## [Data Sources](https://spark.apache.org/docs/3.5.4/sql-data-sources.html)
- 查看支持的配置

进入对应的datasource 查看Data Source Option
<Catalog />