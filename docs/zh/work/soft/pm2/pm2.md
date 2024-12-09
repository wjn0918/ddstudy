# install 






# spark

pm2 start '/usr/local/soft/spark-3.2.2-bin-hadoop3.2/bin/spark-submit --master local[4] --class org.example.HelloWorld /usr/local/soft/spark-3.2.2-bin-hadoop3.2/helloWorld-1.0-SNAPSHOT.jar' --name spark
pm2 save --force
systemctl enable pm2-root



pm2 delete all
pm2 logs spark


# nacos

pm2 start '/usr/local/nacos/bin/startup.sh' --name nacos