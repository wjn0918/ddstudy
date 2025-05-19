---
title: 案例
icon: lightbulb
---


## update

```

UPDATE t_vehicle_bike_info AS t
SET phone = t1.phone
FROM (
    select job_no from t_vehicle_bike_info where deleted= 0 and phone = ''
) AS t2
LEFT JOIN (
    select job_no, phone from t_info_student where workspace_id = 'HZBB' and phone != ''
) AS t1 on t2.job_no = t1.job_no
WHERE t.job_no = t2.job_no
```


select client_addr, count(1) from pg_stat_activity group by client_addr



show max_connections;


alter system set max_connections=1000;