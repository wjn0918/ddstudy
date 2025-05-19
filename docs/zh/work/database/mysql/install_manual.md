## rpm 安装
```
# 移除mariadb依赖
yum -y remove mariadb-libs-*.el7.x86_64
for i in `ls`; do rpm -i $i --force --nodeps; done;


systemctl start mysqld
more /var/log/mysqld.log | grep root@localhost | awk -F 'root@localhost: ' '{print $2}'


ALTER USER USER() IDENTIFIED BY 'Mysql@2023';
grant all on *.* to root@'%' identified by 'Mysql@2023' with grant option;
flush privileges;
```

## 创建用户

```
create database hive default character set utf8;
CREATE USER 'hive'@'%' IDENTIFIED BY 'Hive@2023';
GRANT ALL PRIVILEGES ON hive. * TO 'hive'@'%' IDENTIFIED by 'Hive@2023';
FLUSH PRIVILEGES;
```


## client 安装
```
yum remove -y mariadb-libs-*.el7.x86_64
rpm -ivh mysql-community-common-8.0.34-1.el7.x86_64.rpm 
rpm -ivh mysql-community-client-plugins-8.0.34-1.el7.x86_64.rpm
rpm -ivh mysql-community-libs-8.0.34-1.el7.x86_64.rpm 
rpm -ivh mysql-community-client-8.0.34-1.el7.x86_64.rpm 
```
