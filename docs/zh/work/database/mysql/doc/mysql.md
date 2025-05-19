# 删除长时间查询

```
	select * from information_schema.INNODB_TRX
	
	kill 11310238
```


# jdbc 安装

rpm -qpl mysql-connector-java-8.0.16-1.el7.noarch.rpm


# for update

for update是在数据库中上锁用的，可以为数据库中的行上一个排它锁。当一个事务的操作未完成时候，其他事务可以读取但是不能写入或更新

> select * from table where xxx for update


# windows 重置mysql8.0密码

> C:\Program Files\MySQL\MySQL Server 8.0\bin>mysqld.exe --defaults-file="C:\ProgramData\MySQL\MySQL Server 8.0\my.ini" --console --skip-grant-tables --shared-memory

然后, 启动另一个 CMD 命令行, 输入 mysql -u root 直接登陆, 接着输入以下命令, 将 root 密码置为空
> UPDATE mysql.user SET authentication_string='' WHERE user='root' and host='localhost';


最后, 关闭两个 CMD , 通过 net start mysql 启动 mysql 服务, 输入 mysql -u root 直接登陆, 通过以下命令设置 root 用户的密码
ALTER USER 'root'@'localhost' IDENTIFIED BY '123456';


# linux 重置mysql8.0.32密码

systemctl stop mysqld

vi /etc/my.cnf

新增skip-grant-tables

UPDATE mysql.user SET authentication_string='' WHERE user='root' and host='%';
flush privileges;


ALTER USER 'root'@'%' IDENTIFIED BY 'Mysql@2023';


* jdbc 编码使用utf8mb4  因为数据中包含了表情符号或一些特殊字符  character_set_server=utf8mb4


# 数据库备份

mysqldump --default-character-set=utf8mb4 --host=192.168.3.85 -uroot -p123456 -P3307 --opt cs | gzip > cs.sql.gz

gzip -d cs.sql.gz

恢复
windows
在终端运行  ./mysql.exe -u root -p123456 -P 3307 zjioc < "D:\zjioc.sql20231009"

linux

mysql -u root -p report_data < report_data20231104.sql






# 查看配置

show VARIABLES 




# binlog 恢复


show master logs;  // 该结果返回的即为mysql记录的所有binlog文件

show master status;  // 该结果返回的即为当前mysql的操作所记录的binlog子文件



# 查看连接

SELECT substring_index(host, ':',1) AS host_name,state,count(*) FROM information_schema.processlist GROUP BY state,host_name;


# 更新

```
update  vehicle_info tt
left join 
(
select t.user_id, t.a,t1.user_id as c, t1.nick_name from
(select user_id, nick_name, plate_no, lpad(user_id, 6, 0) as a from vehicle_info  where (user_id REGEXP '[^0-9.]')=0) t 
left join 
(
select user_id, nick_name from sys_user
) t1
on t.a = t1.user_id
where t1.user_id is not null
) tt1
on tt.user_id = tt1.user_id
set tt.nick_name = tt1.nick_name
where  tt.vehicle_id > ''


```


# 日期

```
date_format(str_to_date("2023-11-21T22:52:56.470+08:00", '%Y-%m-%dT%H:%i:%s.%f+08:00'), '%Y-%m-%d') = '2023-11-21'
```


# 替换最后一个,

5.7
```
if(right(vehicle_photo, 1) = ',', 
	substr(vehicle_photo, 1 , LENGTH(vehicle_photo) - 1), 
	vehicle_photo
)
```

8
```
regexp_replace(a,'(.*)(,)', '$1') as b
```