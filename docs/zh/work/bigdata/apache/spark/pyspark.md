---
title: PySpark
---





## 表结构定义


```
schema = "id int, name string, age int"
```

::: tabs

@tab mock

```
data = [[1, "张三", 12],[2, "李四", 14]]
spark.createDataFrame(data,schema).show()
```

@tab csv

```
spark.read.schema(schema).csv('data.csv').show()
```

:::

## Row

A row in DataFrame. The fields in it can be accessed:

- like attributes (row.key)

- like dictionary values (row[key])

```
from pyspark.sql import Row
r1 = Row(name='zs', age=12)
r1.name
r1['name']
```







## 递归查询子元素

```
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql import DataFrame
from pyspark.sql.functions import broadcast
from pyspark.sql.types import StringType, ArrayType, IntegerType

# spark = (
#     SparkSession.builder.remote("sc://192.168.3.12:15002").getOrCreate()
# )

spark = SparkSession.builder.getOrCreate()

# 创建示例数据框
data = [
    (1, 'A', None),
    (2, 'B', 1),
    (3, 'C', 1),
    (4, 'D', 2),
    (5, 'E', 2),
    (6, 'F', 3)
]
columns = ["dept_id", "dept_type", "parent_id"]

df = spark.createDataFrame(data, columns)

df_c = df.toPandas()

df.createOrReplaceTempView("t_cs")

df_b = spark.sparkContext.broadcast(df_c)


def get_children(dept_id):
    _childrens = []
    def _get_children(dept_id):
        nonlocal _childrens
        _df = df_b.value
        df_filtered = _df[_df["parent_id"] == dept_id]
        dept_type = _df[_df["dept_id"] == dept_id]["dept_type"].values[0]
        if len(df_filtered) > 0:
            _childrens.extend(df_filtered["dept_type"].tolist())
            df_filtered.apply(lambda _data: _get_children(_data["dept_id"]), axis=1)
        else:
            _childrens.append(str(dept_type))
    _get_children(dept_id)
    return ",".join(set(_childrens))


def add_one(s:int) -> int:
    print(df_b.value)
    return s + len(df_b.value)

spark.udf.register("add_one", lambda x: add_one(x))
spark.udf.register("get_children", lambda x: get_children(x))

spark.sql("""

select dept_id, add_one(dept_id)
 
 ,get_children(dept_id) 
 
 from t_cs
""").show()

```