---
title: DDL
---


```
ALTER TABLE your_table_name CHANGE old_column_name new_column_name new_data_type [COMMENT 'comment'];
```

create table t_1 (name string) partitioned by (dt string) stored as orc; 