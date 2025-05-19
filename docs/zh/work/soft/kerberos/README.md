---
title: Kerberos
---

```
操作                                    命令
启动kdc服务                          systemctl start krb5kdc
启动kadmin服务                       systemctl start kadmin
进入kadmin                           kadmin.local / kadmin
创建数据库                           kdb5_util create -r EXAMPLE.COM -s
修改当前密码                         kpasswd
测试keytab可用性                     kinit -k -t /home/xiaobai/xb.keytab xiaobai@EXAMPLE.COM
查看当前票据                         klist
查看keytab                           klist -e -k -t /home/xiaobai/xb.keytab
通过keytab文件认证登录          kinit -kt /home/xiaobai/xb.keytab xiaobai@EXAMPLE.COM
通过密码认证登录                  kinit xiaobai@EXAMPLE.COM / kint xiaobai
清除缓存                              kdestroy

kadmin模式下常用命令：

操作                                    命令
查看principal                       listprincs
生成随机key的principal       addprinc -randkey root/admin@EXAMPLE.COM
生成指定key的principal         addprinc -pw xxx root/admin@EXAMPLE.COM
修改root/admin的密码           cpw -pw xxx root/admin
添加/删除principal              addprinc/delprinc root/admin
直接生成到keytab                    ktadd -k /home/xiaobai/xb.keytab xiaobai@EXAMPLE.COM

xst -norandkey -k /home/xiaobai/xb.keytab xiaobai@EXAMPLE.COM

注意：在生成keytab文件时需要加参数"-norandkey"，否则导致直接使用kinit xiaobai@EXAMPLE.COM初始化时提示密码错误。

设置密码策略(policy)          addpol -maxlife "90 days" -minlife "75 days" -minlength 8 -minclasses 3 -maxfailure 10 -history 10 user
修改密码策略                       modpol -maxlife "90 days" -minlife "75 days" -minlength 8 -minclasses 3 -maxfailure 10 user
添加带有密码策略                addprinc -policy user hello/admin@EXAMPLE.COM
修改用户的密码策略             modprinc -policy user1 hello/admin@EXAMPLE.COM
删除密码策略                       delpol [-force] user

备注：Kerberos进入admin管理模式需要使用root用户。

```