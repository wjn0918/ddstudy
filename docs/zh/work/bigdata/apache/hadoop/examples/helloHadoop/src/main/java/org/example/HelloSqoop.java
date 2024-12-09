package org.example;

import org.apache.hadoop.conf.Configuration;

public class HelloSqoop {

    public static void main(String[] args) {

        Configuration.addDefaultResource("hello-hadoop.xml");
        Configuration conf = new Configuration();
        String v = conf.get("cs");
        System.out.println(v);



    }
}
