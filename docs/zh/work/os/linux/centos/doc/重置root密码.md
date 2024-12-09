https://blog.csdn.net/gnail_oug/article/details/94721777


e

LANG=en_US.UTF-8，在后面追加rw single init=/bin/bash,然后按ctrl+x重启系统

passwd


4、如果开启了SELinux，执行命令touch /.autorelabel命令

5、输入exec /sbin/init命令重启系统

6、使用新设置的密码进入系统之后，为了安全起见，可以输入reboot重新启动一次系统。