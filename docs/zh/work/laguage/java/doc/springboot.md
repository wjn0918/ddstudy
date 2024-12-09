# 文件读取

```
    @Autowired
    private ResourceLoader resourceLoader;

    Resource resource = resourceLoader.getResource("classpath:dic/dic.csv");

```



# bean 

•@Lazy：延迟初始化 Bean。  
•@Profile：根据不同的环境配置加载不同的 Bean。  
•@DependsOn：指定 Bean 之间的依赖关系。  
•@Order：指定 Bean 的初始化顺序。  
•@PostConstruct 和 @PreDestroy：在 Bean 初始化后和销毁前执行特定操作。

# @Autowired

如果 Spring 没有其他提示，将会按照需要注入的变量名称来寻找合适的 bean


@Qualifier 可以指定bean


```
package cn.shingi.sr.source;

import org.apache.spark.streaming.api.java.JavaReceiverInputDStream;
import org.apache.spark.streaming.api.java.JavaStreamingContext;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class SocketSource {


    @Autowired
    private JavaStreamingContext ssc;

    @Bean
    public JavaReceiverInputDStream<String> socketData5555(){
        return ssc.socketTextStream("192.168.3.204", 5555);
    }

    @Bean
    public JavaReceiverInputDStream<String> socketData4444(){
        return ssc.socketTextStream("192.168.3.204", 4444);
    }


}





@Configuration
public class ZdrysbJob {

    @Autowired
    private SQLContext spark;

    @Autowired
    private JavaReceiverInputDStream<String> socketData5555;

    @Autowired
    private JavaReceiverInputDStream<String> socketData4444;




    public void run(){
        socketData5555.print();

        socketData4444.print();



    }

}



```
