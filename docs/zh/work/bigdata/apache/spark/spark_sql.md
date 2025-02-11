---
title: SparkSql
---


## 通过java bean 进行查询

```
@Data
@FieldNameConstants
class Person{
    private String name;

}


Field[] fields = Person.Fields.class.getFields();
List<String> collect = Arrays.stream(fields).map(field -> {
    return field.getName();
}).collect(Collectors.toList());

df.selectExpr(collect.toArray(new String[0])).show();


```


## 日期格式化




* utc 格式转timestamp

select from_utc_timestamp('2023-11-03T09:51:59+08:00', 'UTC')



* ISO8601时间格式 转  timestamp

from_utc_timestamp('2023-08-23T12:34:56.789Z', 'UTC')


select date_format(from_utc_timestamp('2023-08-10T09:40:52+08:00', "Asia/Shanghai"), 'yyyy-mm-dd');



# spark sql时区问题

mysql 查询时区  

show variables like '%time_zone%'

spark.conf.set("spark.sql.session.timeZone", "CST")


# 正则

\d 需要使用[0-9] 来代替

# with

```
with
    t1 as (),
    t2 as ()

select t1 left join t2
```

# str array to array

```
select from_json("[{'id': '123', 'planName': 'name'}]", 'ARRAY<struct<id:string, planName:string>>' ) as a;

```