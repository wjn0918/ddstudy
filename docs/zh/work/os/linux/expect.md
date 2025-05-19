---
title: expect脚本
---


```

#!/usr/bin/expect

set timeout 1

#获取外界传递进来的ip参数
set hostip [lindex $argv 0]

#获取外界传递进来的用户名
set username [lindex $argv 1]

#获取外界传递进来的密码参数
set passwd [lindex $argv 2]

#获取外界传递进来的命令参数
set user [lindex $argv 3]

#获取外界传递进来的命令参数
set pass [lindex $argv 4]

spawn ssh $username@$hostip -p 22
expect {
 "(yes/no)" { send "yes\r"; exp_continue }
 "password:" { send "${passwd}\r" }
}

expect $username@* { send "useradd $user\r" };
expect $username@* { send "passwd $user\r" };
expect "New password:" { send "$pass\r" };
expect "Retype new password:" { send "$pass\r" };

expect $username@* { send exit\r };
expect eof;

```


```
#!/usr/bin/expect

set timeout 1

#获取外界传递进来的ip参数
set hostip [lindex $argv 0]

#获取外界传递进来的用户名
set username [lindex $argv 1]

#获取外界传递进来的密码参数
set passwd [lindex $argv 2]

#获取外界传递进来的命令参数
set cmd [lindex $argv 3]


spawn ssh $username@$hostip -p 22
expect {
 "(yes/no)" { send "yes\r"; exp_continue }
 "password:" { send "${passwd}\r" }
}

expect $username@* { send "$cmd\r" };
expect $username@* { send exit\r };
expect eof;

```


```
#!/bin/bash

#判断传入的参数是否满足

if [ "$#" -ne 2 ]
  then
     echo "错误"
     exit
fi

#获取参数
#服务器信息文件
filename=$1
#传入执行的命令
cmd=$2

#获取当前目录
cwd=$(pwd)
cd $cwd

#构建文件全路径
serverlistfile="$cwd/$filename"

#判断此文件是否存在
if [ ! -e $serverlistfile ]
  then
     echo 'serverlistfile not exist';
     exit
fi

#读取文件内容进行循环处理，注意hostips 最后需要有行空的
while read LINE
   do
      if [ -n "$LINE" ]
         then
             echo "********line***********" $LINE
             echo "********cmd************" $cmd
           #循环批量执行命令
           /usr/bin/expect ./bulkshell.expect $LINE "$cmd"
           #判断是否执行成功
           if [ $? -eq 0 ]
              then
                 echo $cmd "done!"
           else
                 echo "error: $?"
           fi
      fi
done < $serverlistfile


```