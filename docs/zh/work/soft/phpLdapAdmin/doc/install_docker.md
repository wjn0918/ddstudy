docker run -dit \
    -p 9999:80 \
    --link ldap \
    --name ldap_mgr \
    --env PHPLDAPADMIN_HTTPS=false \
    --env PHPLDAPADMIN_LDAP_HOSTS=ldap \
    --restart always \
    --detach osixia/phpldapadmin