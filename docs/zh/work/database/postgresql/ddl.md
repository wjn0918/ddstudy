---
title: ddl
icon: lightbulb
---

* 查询视图名

SELECT table_name AS view_name
FROM information_schema.views
WHERE table_schema NOT IN ('pg_catalog', 'information_schema')
ORDER BY view_name;