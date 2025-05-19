---
title: 使用
---

## 查看文件夹中文件后缀有哪些
```
ls | grep '\.' | sed 's/.*\.//' | sort | uniq

```

## 多行写入文件

```
cat >> filename <<EOF

内容

EOF


```


# sed 

sed -i 's|http://localhost|http://127.0.0.1|g' cs.txt

分割符除了竖线 |，您还可以使用其他字符作为分隔符，例如逗号 ,、分号 ; 或者任何其他不会出现在要替换的字符串中的字符



# find

find ./ -type f -name '*.zip' -exec ls {} \;

-type f  普通文件
-exec 执行命令
{} 占位符





# 比较目录文件不同


diff -qr dss dss1 | grep "Only in dss"

# 启动后台进程

```
nohup  命令  2>&1 > app.out &
```



0 2 * * * /bin/bash /path/to/back.sh



# 数据库备份
```
# 获取当前日期并格式化为YYYYMMDD
current_date=$(date +"%Y%m%d")

# 打印当前日期
echo $current_date


mysqldump --default-character-set=utf8mb4 --host=172.23.0.199 -uroot -pXinyi_2023 -P3308 --opt zjioc | gzip > /home/backup/mysql/zjioc.sql$current_date.gz

# 删除七天前文件
find /home/backup/mysql/ -type f -mtime +7 -exec rm {} \;

```


# nginx配置文件备份

```
root_dir="/data/backup/nginx/server200"
# 远程服务器IP地址
remote_server="172.23.0.200"
# 远程SSH端口
remote_ssh_port="55555"
user="root"

year=$(date +%Y)
month=$(date +%m)
day=$(date +%d)
hour=$(date +%H)

# 构造本地备份目录路径
local_backup_dir="$root_dir/$year/$month/$day"

# 构造远程nginx.conf路径
remote_nginx_conf="/usr/local/nginx/conf/nginx.conf"

# 检查本地目录是否存在，如果不存在则创建
if [ ! -d "$local_backup_dir" ]; then
    mkdir -p "$local_backup_dir"
fi

# 使用scp从远程服务器复制nginx.conf文件到本地备份目录，指定端口
scp -P $remote_ssh_port "$user@$remote_server:$remote_nginx_conf" "$local_backup_dir/nginx.conf.$hour.bak"

# 使用rsync从远程服务器复制conf.d目录到本地备份目录，指定端口
rsync -a -e "ssh -p $remote_ssh_port" "$user@$remote_server:/usr/local/nginx/conf/conf.d/" "$local_backup_dir/conf.d_$hour/"


```