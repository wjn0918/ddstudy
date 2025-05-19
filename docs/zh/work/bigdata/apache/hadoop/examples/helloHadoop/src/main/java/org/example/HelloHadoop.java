package org.example;

import org.apache.hadoop.util.ToolRunner;

public class HelloHadoop {

    public static void main(String[] args) throws Exception {

        MyTool myTool = new MyTool();

        ToolRunner.run(myTool, args);


    }
}
