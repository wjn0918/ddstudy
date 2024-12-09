
#### 2.5 安装phpLdapAdmin

```shell
#安装-------
yum -y install httpd php php-ldap php-gd php-mbstring php-pear php-bcmath php-xml
#需要额外yum源，安装方式：yum localinstall http://rpms.famillecollet.com/enterprise/remi-release-7.rpm
#或带安装包，unzip包里是rpm包
yum install -y phpldapadmin


#配置---------
#修改phpldapadmin.conf配置如下：
cat /etc/httpd/conf.d/phpldapadmin.conf
Alias /phpldapadmin /usr/share/phpldapadmin/htdocs
Alias /ldapadmin /usr/share/phpldapadmin/htdocs
<Directory /usr/share/phpldapadmin/htdocs>
<IfModule mod_authz_core.c>
# Apache 2.4
Require all granted
</IfModule>
<IfModule !mod_authz_core.c>
# Apache 2.2
Order Deny,Allow
Deny from all
Allow from 127.0.0.1
Allow from ::1
</IfModule>
</Directory>


#修改相应的login参数
#创建软连接
cd /var/www/html && ln -snf /usr/share/phpldapadmin .

#修改配置397到403行
vim /var/www/html/phpldapadmin/config/config.php

$servers->setValue('login','attr','dn');
$servers->setValue('login','attr','uid');

/* Base DNs to used for logins. If this value is not set, then the LDAP server
   Base DNs are used. */
$servers->setValue('login','base',array('dc=hadoop,dc=com'));



#启动
systemctl start httpd
# 设置开机启动
systemctl enable httpd

访问http://xxx.xxx.xxx.xxx/ldapadmin
```

