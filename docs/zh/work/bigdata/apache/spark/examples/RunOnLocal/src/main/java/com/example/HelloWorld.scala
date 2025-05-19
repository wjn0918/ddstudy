package com.example

import org.apache.spark.SparkConf
import org.apache.spark.sql.SparkSession

object HelloWorld {
  def main(args: Array[String]): Unit = {

    val spark = SparkSession
      .builder()
      .appName("Spark SQL basic example")
      .master("local[4]")
      .getOrCreate()

    val df = spark.read.csv("file:///D:\\cs\\20230214\\面试作业\\20220518_0902.CSV")
    df.show()

  }

}
