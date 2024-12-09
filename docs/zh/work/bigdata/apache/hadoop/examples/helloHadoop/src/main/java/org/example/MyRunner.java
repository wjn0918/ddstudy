package org.example;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.util.Tool;

public class MyRunner implements Tool {


    public int run(String[] strings) throws Exception {
        return 0;
    }

    public void setConf(Configuration configuration) {

    }

    public Configuration getConf() {
        return null;
    }
}
