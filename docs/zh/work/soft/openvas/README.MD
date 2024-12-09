docker run -d -p 1443:443 -e PUBLIC_HOSTNAME=192.168.3.204 -e LANG=zh_CN.UTF-8 -e LANGUAGE=zh_CN:zh -e LC_ALL=zh_CN.UTF-8  --name openvas mikesplain/openvas

apt-get update
apt-get install -y language-pack-zh-hans
echo 'LANG=zh_CN.UTF-8' > /etc/default/locale

update-locale LANG=zh_CN.UTF-8
docker restart openvas
