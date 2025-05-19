# 服务端

```shell
yum install krb5-server krb5-libs krb5-workstation -y

# 创建数据库,设置密码：123
kdb5_util create -r HADOOP.COM -s


# 修改 /etc/krb5.conf
cat > /etc/krb5.conf << EOF
[libdefaults]
  renew_lifetime = 7d
  forwardable = true
  default_realm = HADOOP.COM
  ticket_lifetime = 24h
  dns_lookup_realm = false
  dns_lookup_kdc = false
  default_ccache_name = /tmp/krb5cc_%{uid}
  #default_tgs_enctypes = aes des3-cbc-sha1 rc4 des-cbc-md5
  #default_tkt_enctypes = aes des3-cbc-sha1 rc4 des-cbc-md5
  udp_preference_limit = 1
  kdc_timeout = 3000
[logging]
  default = FILE://var/log/krb5kdc.log
  admin_server = FILE:/var/log/kadmind.log
  kdc = FILE:/var/log/krb5kdc.log

[realms]
  HADOOP.COM = {
    admin_server = server204.bigdata.local
    kdc = server204.bigdata.local
  }
[domain_realm]
  .hadoop.com = HADOOP.COM
  hadoop.com = HADOOP.COM

EOF


# 修改 /var/kerberos/krb5kdc/kdc.conf
cat > /var/kerberos/krb5kdc/kdc.conf << EOF
[kdcdefaults]
 kdc_ports = 88
 kdc_tcp_ports = 88

[realms]
 EXAMPLE.COM = {
  #master_key_type = aes256-cts
  acl_file = /var/kerberos/krb5kdc/kadm5.acl
  dict_file = /usr/share/dict/words
  admin_keytab = /var/kerberos/krb5kdc/kadm5.keytab
  supported_enctypes = aes256-cts:normal aes128-cts:normal des3-hmac-sha1:normal arcfour-hmac:normal camellia256-cts:normal camellia128-cts:normal des-hmac-sha1:normal des-cbc-md5:normal des-cbc-crc:normal
 }

EOF


# 启动服务 
systemctl start krb5kdc
systemctl start kadmin
systemctl enable krb5kdc
systemctl enable kadmin


# 创建管理用户(建议手动输入密码)
kadmin.local -q "addprinc admin/admin"

# 修改 /var/kerberos/krb5kdc/kadm5.acl
*/admin@HADOOP.COM      *

# 重启服务生效
systemctl restart kadmin
systemctl restart krb5kdc
```



# 客户端

```shell
yum -y install krb5-workstation

# copy /etc/krb5.conf

scp [server_ip]:/etc/krb5.conf /etc/krb5.conf
```

