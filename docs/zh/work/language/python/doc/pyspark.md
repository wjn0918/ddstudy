---
title: pyspark
---

* An error occurred while calling None.org.apache.spark.api.java.JavaSparkContext.

java的JDK版本问题，由于mac中同时存在1.8（JDK1.8就是JDK8）和18的版本，将JDK的环境变量设置为1.8，降低版本即可 

* AttributeError: module 'pypandoc' has no attribute 'convert'

使用3.2.4版