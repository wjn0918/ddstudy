---
title: Maven
---

mvn clean install -T 1C -Dmaven.test.skip=true -Dmaven.compile.fork=true



## 开启多线程编译：

-Dmaven.compile.fork=true

##  每核增加一个线程进行构建：

-T 1C

## 输出依赖
mvn dependency:tree > tree.txt

## Do not recurse into sub-projects
    mvn -N  
                