    docker run -dit \
    -p 389:389 \
    -v /data/ldap/ldap:/var/lib/ldap \
    -v /data/ldap/slapd.d:/etc/ldap/slapd.d \
    --name ldap \
    --env LDAP_TLS=false \
    --env LDAP_ORGANISATION="fd" \
    --env LDAP_DOMAIN="fd.com" \
    --env LDAP_BASE_DN="dc=fd,dc=com" \
    --env LDAP_ADMIN_PASSWORD="123456" \
    --env LDAP_CONFIG_PASSWORD="123456" \
    --restart always \
    --detach osixia/openldap


配置LDAP组织者：LDAP_ORGANISATION  
配置LDAP域：LDAP_DOMAIN  
配置LDAP密码：LDAP_ADMIN_PASSWORD  
默认登录用户名：admin  