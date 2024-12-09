# 安装


1. [下载安装包](http://nginx.org/)
2. 解压
3. 安装相关依赖

   yum -y install gcc pcre-devel openssl openssl-devel
4. 编译nginx

   ./configure --prefix=解压到的文件目录（安装目录，不需要创建）  --without-http_rewrite_module --without-http_gzip_module
5. ./configure --prefix=/usr/local/nginx/nginx1.14.2 --without-http_rewrite_module --with-http_gzip_static_module --with-stream --with-pcre 

例：

    ./configure --prefix=/usr/local/nginx/nginx1.6.3 --without-http_rewrite_module --without-http_gzip_module --with-stream

5. 安装

   make install
6. 启动

   * 进入sbin 目录
   * 启动./nginx
   * 关闭 ./nginx -s quit
   * 重启 ./nginx -s reload
7. 创建软连接（可选）

ln  -s  [源文件或目录]  [目标文件或目录]

例:

    ln -s /usr/local/nginx/nginx1.6.3/sbin/nginx /usr/local/bin/nginx




# https

```
openssl genpkey -algorithm RSA -out ./private.key


openssl req -new -key ./private.key -out ./certificate.csr

openssl x509 -req -in ./certificate.csr -signkey ./private.key -out ./certificate.crt


hingi@2023


ssl_certificate    ./ssl/certificate.crt;
ssl_certificate_key  ./ssl/private.key;

```


# 服务转发




# 重定向添加端口

```
server {
       listen 80;
       server_name sx.fdstack.com;
       location / {
          rewrite .* http://$host:9100/ent/index.html permanent;
       }
   }
```


# 挂载资源
```
server {
    listen 88;
    location / {
        root /data/EMR;
        autoindex on;
    }
}

```

# basic认证
```
1. 生成一个账户密码文件 pass_file
htpasswd -c -d /etc/nginx/conf.d/pass_file fd

fd ---用户名

2. nginx.conf

auth_basic "need user and password";
auth_basic_user_file /etc/nginx/conf.d/pass_file;

实例
```
location / {
    auth_basic "need user and password";
    auth_basic_user_file /etc/nginx/conf.d/pass_file;
    root   /usr/share/nginx/html;
    index  index.html index.htm;
}
```
```


# ssl 认证

生成ssl.pem文件
openssl x509 -inform PEM -in ssl.crt > ssl.pem


# 配置systemctl 

cp nginx.service /usr/lib/systemd/system/
systemctl daemon-reload
systemctl enable nginx.service
systemctl start nginx.service


# 允许跨域