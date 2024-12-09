# 代码规范化

spotless-maven-plugin

# 匿名类
创建子类对象时，除了使用父类地构造方法外还有类体，此类体被认为是一个子类去掉类声明后地类体，称为匿名类

没有显式地声明一个类地子类，又想使用子类创建一个对象
适合创建只需要一次使用地类


# 打包


jar -cf cs.jar -C . org\\example\\flume

# windows运行jar

java -cp nh-spark-1.0-SNAPSHOT-assembly.jar;D:\soft\spark-3.2.2-bin-hadoop3.2\jars\* -Dspark.master=local[4] -Dconf_file=prod -Doverwrite=flase cn.shingi.nh.NhSparkApplication --conf_file=prod