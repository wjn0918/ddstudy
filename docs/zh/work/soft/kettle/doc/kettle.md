连接mysql 需要配置useSSL = false characterEncoding=utf8


* repository connection 默认用户密码 admin/admin

* spoon.bat 添加"-Dfile.encoding=UTF-8"

if "%PENTAHO_DI_JAVA_OPTIONS%"=="" set PENTAHO_DI_JAVA_OPTIONS="-Xms1024m" "-Xmx2048m" "-XX:MaxPermSize=256m" "-Dfile.encoding=UTF-8"