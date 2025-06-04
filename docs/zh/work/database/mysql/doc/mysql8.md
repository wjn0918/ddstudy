---
title: Mysql8
---

## 取非空

```
SELECT COALESCE(column1, column2, column3, '所有列都为空') AS first_non_null_value
FROM your_table;
```

## GROUPING SETS

```
-- 同时按多个维度组合进行分组统计
SELECT 
    department, 
    job_title,
    COUNT(*) AS employee_count
FROM 
    employees
GROUP BY 
    GROUPING SETS (
        (department, job_title),
        (department),
        (job_title),
        ()
    );
```

## 设置时区

default-time-zone='+8:00'

set global validate_password.policy=LOW;
set global validate_password.length=4;