---
title: DCL
---

## 数据恢复

```
pg_restore -U postgres -h localhost -p 5432 -d sr_20250221 -F c -t t_access_map  --clean --if-exists school_20250521_020001.dump
```


-t your_table_name：仅恢复指定的表（可多次使用，如 -t table1 -t table2）

--clean：恢复前先删除目标表（避免冲突）

--if-exists：避免表不存在时报错


## 创建用户

CREATE USER username WITH PASSWORD 'PASSWORD';

## 用户赋权

GRANT SELECT ON tablename TO username;