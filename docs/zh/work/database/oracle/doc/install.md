git clone https://github.com/oracle/docker-images.git
cd docker-images/OracleDatabase/SingleInstance/dockerfiles/19.3.0/
wget http://yum.oracle.com/repo/OracleLinux/OL7/latest/x86_64/getPackage/oracle-database-preinstall-19c-1.0-1.el7.x86_64.rpm



https://pkgs.org/download/rlwrap

wget https://dl.fedoraproject.org/pub/epel/7/aarch64/Packages/r/rlwrap-0.43-2.el7.aarch64.rpm

下载  https://download.oracle.com/otn/linux/oracle19c/190000/LINUX.X64_193000_db_home.zip?AuthParam=1692928036_28d0b5e96329c4beecf30e71a31c42ca 放到版本目录

./buildContainerImage.sh -v 19.3.0 -e





https://www.jianshu.com/p/b683640677c9





mkdir  -p /Users/myz/Docker/Oracle/19.3/
--执行创建
docker run -e TZ="Asia/Shanghai"  -itd -h ora193 -m 2048m --name ora193 \
  -p 1521:1521 -p 5500:5500 \
  -e ORACLE_SID=mycdb \
  -e ORACLE_PDB=pdb1 \
  -v /Users/myz/Docker/Oracle/19.3/:/opt/oracle/oradata  oracle/database:19.3.0-ee




ORACLE 密码不能带@


docker exec ora193  ./setPassword.sh 123456


sqlplus sys/oracle@//127.0.0.1:1521/mycdb as sysdba
system
123456



https://www.jianshu.com/p/9000cdd58cd8





* navicat no matching authentication protocol

Oracle instant client