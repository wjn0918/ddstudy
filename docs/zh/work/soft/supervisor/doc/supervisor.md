# 操作

supervisorctl reread
supervisorctl update




pip install supervisor
mkdir /etc/supervisord.d/
echo_supervisord_conf > /etc/supervisord.conf


#修改socket文件的mode，默认是0700
sed -i 's/;chmod=0700/chmod=0766/g' /etc/supervisord.conf   

#在配置文件最后添加以下两行内容来包含/etc/supervisord目录
sed -i '$a [include] \
files = /etc/supervisord.d/*.conf' /etc/supervisord.conf





[inet_http_server]
port=*:9001
username=admin
password=123456