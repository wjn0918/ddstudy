# root用户ssh登录不了

需要修改/etc/ssh/sshd_config
permit
service ssh restart 




wsl --shutdown

.wslconfig
https://www.cnblogs.com/sxrhhh/p/17901967.html
[experimental]
networkingMode=mirrored
dnsTunneling=true
firewall=true
autoProxy=true
hostAddressLoopback=true


netsh interface portproxy show all

# netsh interface portproxy add v4tov4 listenport=[win10端口] listenaddress=0.0.0.0 connectport=[虚拟机的端口] connectaddress=[虚拟机的ip]
netsh interface portproxy add v4tov4 listenport=80 listenaddress=0.0.0.0 connectport=80 connectaddress=172.29.41.233