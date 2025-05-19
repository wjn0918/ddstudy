# 用户加入supergroup

* 创建supergroup 
> groupadd supergroup
* 用户添加到supergroup 组
> usermod -a -G supergroup userName
* 检查用户所属组
> id userName
* 同步用户
> hdfs dfsadmin -refreshUserToGroupsMappings
-fs hdfs://localhost:8020


hostnamectl --static set-hostname

# 新增节点
* 安装java 

> yum install -y  java-1.8.0-openjdk.x86_64 java-1.8.0-openjdk-demo  java-1.8.0-openjdk-devel java-1.8.0-openjdk-javadoc




* /etc/hosts增加节点信息
* 更改slaves 添加新增节点
* 防火墙放行

firewall-cmd --permanent --add-port=4000/tcp

> firewall-cmd --permanent --add-rich-rule="rule family="ipv4" source address="server191.bd.jz" accept"
* copy /etc/hadoop
* 更改core-site.xml  和 hdfs-site.xml 的存储位置
* 更改hadoop-env.sh 设置ssh 端口    export HADOOP_SSH_OPTS="-p 7788"

* master 节点启动


* You have not permission to access path 

vi /etc/sysconfig/selinux



# 

hdfs --daemon start datanode