# 启动 Standalone Server 服务
bash ./bin/dolphinscheduler-daemon.sh start standalone-server
# 停止 Standalone Server 服务
bash ./bin/dolphinscheduler-daemon.sh stop standalone-server
# 查看 Standalone Server 状态
bash ./bin/dolphinscheduler-daemon.sh status standalone-server


# 变量

昨天
设置全局参数  dt  =  $[yyyy-MM-dd-1]  使用${dt}




# 设置


dolphinscheduler_env.sh
```
# 时区
SPRING_JACKSON_TIME_ZONE=GMT+8
```

common.properties
development.state=true


# 传递上一月
shell1   
now in $[yyyy-MM-dd]
out_last_month out
```
#!/bin/bash

# 获取当前日期的上一个月
current_date=$(date -d "2023-11-01" +%Y-%m-%d)
last_month=$(date -d "$current_date -1 month" +%Y-%m-%d)
last_month_ym=$(date -d "$current_date -1 month" +%Y-%m)
last_month_year=$(date -d "$last_month" +%Y)
last_month_month=$(date -d "$last_month" +%m)

echo "上一个月的日期为：$last_month"
echo "year: $last_month_year"
echo "month: $last_month_month"

echo "\${setValue(out_last_month=${last_month_ym})}"
echo "\${setValue(out_last_month_year=${last_month_year})}"
echo "\${setValue(out_last_month_month=${last_month_month})}"

```

shell2 

```
echo ${out_last_month}
```



# 参数传递


```
#!/bin/bash

# 输入yyyyMMddHHmmss格式的时间字符串
input_datetime="${now}"

# 提取年、月、日、小时、分钟和秒
year="${input_datetime:0:4}"
month="${input_datetime:4:2}"
day="${input_datetime:6:2}"
hour="${input_datetime:8:2}"
minute="${input_datetime:10:2}"
second="${input_datetime:12:2}"

# 使用date命令将其转换为ISO8601格式
iso8601_datetime=$(date -d "$year-$month-$day $hour:$minute:$second" +"%Y-%m-%dT%H:%M:%S+08:00")

# 计算前10分钟的时间戳
timestamp=$(date -d "$year-$month-$day $hour:$minute:$second" +"%s")
ten_minutes_ago_timestamp=$((timestamp - 600))

# 使用date命令将前10分钟的时间戳转换为ISO8601格式
iso8601_ten_minutes_ago=$(date -d "@$ten_minutes_ago_timestamp" +"%Y-%m-%dT%H:%M:%S+08:00")

echo "输入yyyyMMddHHmmss时间字符串: $input_datetime"
echo "转换为ISO8601格式: $iso8601_datetime"
echo "前10分钟的ISO8601格式: $iso8601_ten_minutes_ago"


echo "\${setValue(start_time=${iso8601_ten_minutes_ago})}"
echo "\${setValue(end_time=${iso8601_datetime})}"

```

```
echo ${output}
```


# 批量删除

删除任务
delete from t_ds_task_instance where name like 'dws_hik_door%' and state = 1  
删除工作流
delete from t_ds_process_instance where name like 'mf_dorm_access_record%' and state = 1