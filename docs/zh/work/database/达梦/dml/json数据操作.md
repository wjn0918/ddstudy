<!--
 * @Author: wjn
 * @Date: 2021-10-14 14:15:36
 * @LastEditors: wjn
 * @LastEditTime: 2021-10-14 14:15:36
-->
```
create table test1 (info varchar(100));
insert into test1 values('{"db_name": "DM","version":8}');

select 
	json_value(info,'$.db_name')
from test1
```