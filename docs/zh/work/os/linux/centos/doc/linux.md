# selinux

setenforce 0


# sftp无法连接


vi /etc/ssh/sshd_config

查找sftp 所在文件是否存在   





# 添加路由

route add -host 192.168.8.65 gw 10.10.3.254

# sudo privilege

echo "deploy ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers



* LC_ALL: cannot change locale (en_US.UTF-8): No such file or directory 

localedef -i en_US -f UTF-8 en_US.UTF-8


# 磁盘挂载

```
lsdisk 
查看未挂载磁盘


All primary partitions are in use
Adding logical partition 7
No free sectors available

分区满了，删除不用的分区

d




查看可以使用的磁盘
fdisk -l 
fdisk /dev/vdc
n
p
回车
回车
回车
t
8e
w


yum -y install lvm2
pvcreate /dev/vdc
mkfs.xfs -f /dev/vdc
mount /dev/vdc /easyv


sudo yum install util-linux

1、首先查看逻辑分区uuid   blkid /dev/vdb1

2、去编辑fstab，照自动挂载的格式写上。（这里推荐用uuid，因为重启后逻辑分区号有改变的风险）

UUID=f221211d-a26c-4852-aece-5207177f97e7 挂载后的路径  ext4 defaults 0 0



https://help.aliyun.com/zh/ecs/system-startup-exceptions-caused-by-incorrect-configuration-of-the-or-etc-or-fstab-file-of-a-linux-instance#:~:text=%E9%97%AE%E9%A2%98%E5%8E%9F%E5%9B%A0%20%E4%B8%80%E8%88%AC%E6%98%AF%E5%9B%A0%E4%B8%BA%20%2Fetc%2Ffstab,%E6%96%87%E4%BB%B6%E4%B8%AD%E5%86%99%E5%85%A5%E4%BA%86%E9%94%99%E8%AF%AF%E7%9A%84%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F%EF%BC%8C%E6%88%96%E8%80%85%E7%A3%81%E7%9B%98%E7%9A%84%E5%88%86%E5%8C%BA%E4%BF%A1%E6%81%AF%E4%B8%8D%E6%AD%A3%E7%A1%AE%E3%80%82%20%2Fetc%2Ffstab%20%E6%96%87%E4%BB%B6%E4%B8%BB%E8%A6%81%E7%94%A8%E4%BA%8E%E4%BF%9D%E5%AD%98%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%9A%84%E7%A3%81%E7%9B%98%E6%8C%82%E8%BD%BD%E4%BF%A1%E6%81%AF%EF%BC%8C%E5%A6%82%E6%9E%9C%E8%AF%A5%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E4%B8%AD%E5%86%99%E5%85%A5%E4%B8%8D%E6%AD%A3%E7%A1%AE%E7%9A%84%E6%8C%82%E8%BD%BD%E4%BF%A1%E6%81%AF%E6%88%96%E8%80%85%E8%AF%A5%E6%96%87%E4%BB%B6%E8%87%AA%E8%BA%AB%E5%AD%98%E5%9C%A8%E8%AE%BF%E9%97%AE%E9%94%99%E8%AF%AF%EF%BC%8C%E4%BE%8B%E5%A6%82%EF%BC%9A%E6%9D%83%E9%99%90%E9%85%8D%E7%BD%AE%E3%80%81%E6%96%87%E4%BB%B6%E4%B8%A2%E5%A4%B1%E7%AD%89%EF%BC%8C%E7%B3%BB%E7%BB%9F%E5%90%AF%E5%8A%A8%E6%97%B6%E5%B0%B1%E5%8F%AF%E8%83%BD%E5%87%BA%E7%8E%B0%E5%BC%82%E5%B8%B8%EF%BC%8C%E5%AF%BC%E8%87%B4%E5%90%AF%E5%8A%A8%E5%A4%B1%E8%B4%A5%E3%80%82

```

# sudo权限

> echo "deploy ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers


# 服务自启

/usr/lib/systemd/system
systemctl daemon-reload

```
[Unit]
Description=My Node.js Application
After=mysqld.service 

[Service]
User=root
WorkingDirectory=/home/soft/report/build
ExecStart=/usr/local/bin/npm run start
ExecStop=/usr/local/bin/npm run stop
Restart=always
RestartSec=10
Environment=NODE_ENV=production
RemainAfterExit=yes   # 解决systemctl在service处于inactive状态时会自动调用ExecStop

[Install]
WantedBy=multi-user.target


```

## nginx服务自启
```

[Unit]
Description=The nginx HTTP and reverse proxy server
After=network-online.target remote-fs.target nss-lookup.target
Wants=network-online.target

[Service]
Type=forking
PIDFile=/run/nginx.pid
# Nginx will fail to start if /run/nginx.pid already exists but has the wrong
# SELinux context. This might happen when running `nginx -t` from the cmdline.
# https://bugzilla.redhat.com/show_bug.cgi?id=1268621
ExecStartPre=/usr/bin/rm -f /run/nginx.pid
ExecStartPre=/usr/sbin/nginx -t
ExecStart=/usr/sbin/nginx
ExecReload=/usr/sbin/nginx -s reload
KillSignal=SIGQUIT
TimeoutStopSec=5
KillMode=mixed
PrivateTmp=true

[Install]
WantedBy=multi-user.target
```


# 快速移动大约40GB的数据
rsync可以在两个目录之间同步数据，并且可以非常高效地处理大文件和大目录

> rsync -avh /source_directory/ /destination_directory/

这个命令会将 /source_directory 中的所有文件和子目录复制到 /destination_directory，并保持文件权限和时间戳。




# 配置本地yum源

https://mirrors.aliyun.com/centos/7/isos/x86_64/

* 创建挂载目录

> mkdir -p /data/yumiso

* 挂载镜像
mount -o loop /root/CentOS-7-x86_64-Everything-1611.iso /data/yumiso

* 注释原始yum
> rename repo repo.bak *.repo
* 新增本地yum
> yum-config-manager --add-repo file:///data/yumiso

# jvm 添加mysql driver

cp mysql-connector-java.jar /usr/lib/jvm/java-1.8.0-openjdk/jre/lib/ext/