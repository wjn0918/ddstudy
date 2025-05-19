windows
注意初始化配置参数
1、大小写敏感
2、字符集
3、VARCHAR类型对象的长度是否以字符 为单位

Linux
1.安装前准备：
[root@node11 dmdbms]# cat /etc/redhat-release

Red Hat Enterprise Linux Server release 7.4 (Maipo)
[root@node11 dmdbms]# cat /proc/cpuinfo

 
model name : Intel(R) Xeon(R) CPU E5-2690 v4 @ 2.60GHz
 
确定操作系统版本为：redhat 7.4   cpu架构为intel x86
 
 
选择与操作系统版本相匹配的达梦数据库版本
 
 
2.修改操作系统参数
1）open file参数
vi /etc/security/limits.conf

加入以下两行：
* hard nofile 65536
* soft nofile 65536

 
2）关闭防火墙（不推荐），或开放5236端口（达梦数据库默认端口）
 systemctl stop firewalld

然后重启服务器
reboot

 
 
 
3.安装数据库软件
 
主要文件有两个：DMInstall.bin   dm.key
 
[root@node10 dminstall]# ./DMInstall.bin

解压安装程序..........
初始化图形界面失败，如果当前监视器窗口不支持图形界面，请进入安装文件所在文件夹并使用"./DMInstall.bin -i"进行命令行安装。
[root@node10 dminstall]# ./DMInstall.bin -i

请选择安装语言(C/c:中文 E/e:英文) [C/c]:C   
解压安装程序..........
欢迎使用达梦数据库安装程序
 
是否输入Key文件路径? (Y/y:是 N/n:否) [Y/y]:Y
请输入Key文件的路径地址 [dm/opt/dminstall/dm.key  
 
有效日期: 2019-03-31
服务器颁布类型: 企业版
发布类型: 试用版
用户名称: 中共湖北省委政法委
授权用户数: 无限制
并发连接数: 无限制
 
是否设置时区? (Y/y:是 N/n:否) [Y/y]:  y
设置时区:
[ 1]: GTM-12=日界线西
[ 2]: GTM-11=萨摩亚群岛
[ 3]: GTM-10=夏威夷
[ 4]: GTM-09=阿拉斯加
[ 5]: GTM-08=太平洋时间（美国和加拿大）
[ 6]: GTM-07=亚利桑那
[ 7]: GTM-06=中部时间（美国和加拿大）
[ 8]: GTM-05=东部部时间（美国和加拿大）
[ 9]: GTM-04=大西洋时间（美国和加拿大）
[10]: GTM-03=巴西利亚
[11]: GTM-02=中大西洋
[12]: GTM-01=亚速尔群岛
[13]: GTM=格林威治标准时间
[14]: GTM+01=萨拉热窝
[15]: GTM+02=开罗
[16]: GTM+03=莫斯科
[17]: GTM+04=阿布扎比
[18]: GTM+05=伊斯兰堡
[19]: GTM+06=达卡
[20]: GTM+07=曼谷，河内
[21]: GTM+08=中国标准时间
[22]: GTM+09=汉城
[23]: GTM+10=关岛
[24]: GTM+11=所罗门群岛
[25]: GTM+12=斐济
[26]: GTM+13=努库阿勒法
[27]: GTM+14=基里巴斯
请选择设置时区 [21]:  21
 
安装类型:
1 典型安装
2 服务器
3 客户端
4 自定义
请选择安装类型的数字序号 [1 典型安装]:  1
所需空间: 827M
 
请选择安装目录 [/opt/dmdbms]:   (此处可另设置安装目录，输入指定目录的绝对路径即可)
可用空间: 44G
是否确认安装路径? (Y/y:是 N/n:否)  [Y/y]:  y
 
安装前小结
安装位置: /opt/dmdbms
所需空间: 827M
可用空间: 44G
版本信息: 企业版
有效日期: 2019-03-31
安装类型: 典型安装
是否确认安装? (Y/y:是 N/n:否):
是否确认安装? (Y/y:是 N/n:否):y
2018-10-12 18:46:32
[INFO] 安装 default 模块...
2018-10-12 18:46:32
[INFO] 安装达梦数据库...
2018-10-12 18:46:34
[INFO] 安装 server 模块...
2018-10-12 18:46:34
[INFO] 安装 client 模块...
2018-10-12 18:46:34
[INFO] 安装 drivers 模块...
2018-10-12 18:46:34
[INFO] 安装 manual 模块...
2018-10-12 18:46:34
[INFO] 安装 service 模块...
2018-10-12 18:46:37
[INFO] 创建dmdba系统管理员完成。
2018-10-12 18:46:37
[INFO] 正在启动DmAPService服务...
2018-10-12 18:46:37
[INFO] 启动DmAPService服务成功。
2018-10-12 18:46:37
[INFO] 移动ant日志文件。
2018-10-12 18:46:37
[INFO] 安装达梦数据库完成。
 
安装结束
 
 
4. 初始化数据库实例(以dmdba用户操作)
 
修改dmdba用户密码
[root@node10 bin]# passwd dmdba

更改用户 dmdba 的密码
 
改为dameng2018
 
su - dmdba

 
cd /opt/dmdbms/bin

 
[dmdba@node10 bin]# 
./dminit path=/home/dmdba/dmdata page_size=16 extent_size=16 case_sensitive=n charset=1 length_in_char=1 

(case_sensitive参数为大小写敏感参数，可选值：Y/N，1/0，如AbC=ABC=abc，charset参数为字符集参数，可选值：0[GB18030]，1[UTF-8]，2[EUC-KR])
initdb V7.6.0.96-Build(2018.09.19-97292)ENT
db version: 0x7000a
License will expire on 2019-03-31
 
 log file path: /home/dmdba/dmdata/DAMENG/DAMENG01.log
 
 
 log file path: /home/dmdba/dmdata/DAMENG/DAMENG02.log
 
write to dir [/home/dmdba/dmdata/DAMENG].
create dm database success. 2018-10-12 18:55:52
 
5. 注册linux服务


dm7 

```
cd /opt/dmdbms/script/root


[root@node10 root]# ./dm_service_installer.sh  -t dmserver -p DMSERVER -i /home/dmdba/dmdata/DAMENG/dm.ini -m open

Created symlink from /etc/systemd/system/multi-user.target.wants/DmServiceDMSERVER.service to /usr/lib/systemd/system/DmServiceDMSERVER.service.
创建服务(DmServiceDMSERVER)完成
 
 
关于此脚本的用法，参见/opt/dmdbms/doc/special/DM7_Linux服务脚本手册.pdf
```

dm8 注册
```
./dm_service_installer.sh -t dmserver -dm_ini /home/dmdba/dmdata/DAMENG/dm.ini -p DMSERVER
 
```
6.使用服务脚本后台启动数据库
 
root用户
[root@node10 bin]# systemctl status DmServiceDMSERVER.service

● DmServiceDMSERVER.service - DmServiceDMSERVER
   Loaded: loaded (/usr/lib/systemd/system/DmServiceDMSERVER.service; enabled; vendor preset: disabled)
   Active: inactive (dead)
 
 
[root@node10 bin]# systemctl start DmServiceDMSERVER.service


[root@node10 bin]# systemctl status DmServiceDMSERVER.service

● DmServiceDMSERVER.service - DmServiceDMSERVER
   Loaded: loaded (/usr/lib/systemd/system/DmServiceDMSERVER.service; enabled; vendor preset: disabled)
   Active: active (exited) since 五 2018-10-12 19:12:50 CST; 3s ago
  Process: 9666 ExecStart=/opt/dmdbms/bin/DmServiceDMSERVER start (code=exited, status=0/SUCCESS)
 Main PID: 9666 (code=exited, status=0/SUCCESS)
 
10月 12 19:12:35 node10 systemd[1]: Starting DmServiceDMSERVER...
10月 12 19:12:35 node10 su[9695]: (to dmdba) root on none
10月 12 19:12:35 node10 DmServiceDMSERVER[9666]: Starting DmServiceDMSERVER: 上一次登录：五 10月 12 18:46:37 CST 2018
10月 12 19:12:50 node10 DmServiceDMSERVER[9666]: [11B blob data]
10月 12 19:12:50 node10 systemd[1]: Started DmServiceDMSERVER.
 
 
 
dmdba用户
[root@node10 bin]# su - dmdba

上一次登录：五 10月 12 19:14:27 CST 2018pts/0 上
-sh-4.2$ cd /opt/dmdbms/bin
-sh-4.2$ ./DmServiceDMSERVER restart
Stopping DmServiceDMSERVER:                                [ OK ]
Starting DmServiceDMSERVER:                                [ OK ]
 
7.查看达梦数据库是否启动
-sh-4.2$ ps -ef|grep dmserver

dmdba    10001     1  0 19:18 pts/0    00:00:00 /opt/dmdbms/bin/dmserver /home/dmdba/dmdata/DAMENG/dm.ini -noconsole
dmdba    10073  9857  0 19:20 pts/0    00:00:00 grep --color=auto dmserver
 
8. 修改数据库兼容性参数，针对前期不同数据库进行修改(可以不用修改)
vi /home/dmdba/dmdata/DAMENG/dm.ini

COMPATIBLE_MODE                 =  4                   
 #Server compatible mode, 0:none, 1:SQL92, 2:Oracle, 3:MS SQL Server, 4:MySQL, 5:DM6
 



9. 使用数据库前准备
1）修改数据库redo日志大小
alter database resize logfile 'DAMENG01.log' to 2048;
alter database resize logfile 'DAMENG02.log' to 2048;

 
2) 创建表空间和用户
create tablespace "zfw" datafile 'TEST01.DBF' size 2048 autoextend on next 2048, 'TEST02.DBF' size 2048 autoextend on next 2048;
 
--建议每个用户单独规划一个表空间,便于单独管理
--根据数据量,每个表空间规划多个数据文件,分散io压力
 
CREATE USER TEST IDENTIFIED BY "TEST123456" DEFAULT TABLESPACE TEST;
GRANT DBA TO TEST;       --赋予dba权限
GRANT RESOURCE TO TEST;  --赋予普通权限
 
10. 使用创建的用户登陆数据库使用

function createDb(ms,mm){
    var t = `
    create tablespace "{MS}" datafile '{MS}01.DBF' size 2048 autoextend on next 2048, '{MS}02.DBF' size 2048 autoextend on next 2048;
 
--建议每个用户单独规划一个表空间,便于单独管理
--根据数据量,每个表空间规划多个数据文件,分散io压力
 
CREATE USER {MS} IDENTIFIED BY "{MM}" DEFAULT TABLESPACE {MS};
GRANT DBA TO {MS};       --赋予dba权限
GRANT RESOURCE TO {MS};  --赋予普通权限
    `;
    return t.replace(/{MS}/g,ms).replace(/{MM}/g,mm)
}
createDb('ZFW_WW_SY','ZFW_WW_SY') 
createDb('ZFW_WW_2','ZFW_WW_212#$')





附：
数据库安装说明：
10.205.246.10
10.205.246.11
 
数据库客户端软件安装路径： /opt/dmdbms
数据库日志路径：     /opt/dmdbms/log
数据库文件存放路径： /home/dmdba/dmdata
 
操作系统管理用户: dmdba/dameng2018
数据库管理用户： SYSDBA/SYSDBA

【更改大小写敏感】

dm.ini文件中添加配置参数


create tablespace "ZFW_WW" datafile 'ZFW_WW01.DBF' size 2048 autoextend on next 2048, 'ZFW_WW02.DBF' size 2048 autoextend on next 2048;
CREATE USER "ZFW_WW" IDENTIFIED BY "ZFW_WW_DC" DEFAULT TABLESPACE ZFW_WW;

GRANT DBA TO ZFW_WW;
GRANT RESOURCE TO ZFW_WW
 




卸载：
安装目录中
./uninstall.sh -i

删除/home/dmdba/dmdata/DAMENG路径下的   .DBF文件
 
 
 
 
 
 
 