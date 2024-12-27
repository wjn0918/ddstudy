---
title: SpringBoot
---

## 指定配置文件

:::tabs

@tab IDEA

Environment variable

spring.profiles.active=prod


:::


## 文件读取

```
    @Autowired
    private ResourceLoader resourceLoader;

    Resource resource = resourceLoader.getResource("classpath:dic/dic.csv");

```



## bean 

- @Lazy：延迟初始化 Bean。  
- @Profile：根据不同的环境配置加载不同的 Bean。  
- @DependsOn：指定 Bean 之间的依赖关系。  
- @Order：指定 Bean 的初始化顺序。  
- @PostConstruct 和 @PreDestroy：在 Bean 初始化后和销毁前执行特定操作。

## @Autowired

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


## 日志

### 日志分文件写入

logback-spring.xml

```
<configuration>
    <!-- 定义日志文件路径 -->
    <property name="LOG_PATH" value="./logs" />

    <!-- 控制台日志 -->
    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d{yyyy-MM-dd HH:mm:ss} %-5level [%thread] %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>

    <!-- 文件日志1：INFO级别及以上 -->
    <appender name="FILE_INFO" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>${LOG_PATH}/info.log</file>
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <fileNamePattern>${LOG_PATH}/info.%d{yyyy-MM-dd}.log</fileNamePattern>
            <maxHistory>30</maxHistory>
        </rollingPolicy>
        <encoder>
            <pattern>%d{yyyy-MM-dd HH:mm:ss} %-5level [%thread] %logger{36} - %msg%n</pattern>
        </encoder>
        <filter class="ch.qos.logback.classic.filter.LevelFilter">
            <level>INFO</level>
            <onMatch>ACCEPT</onMatch>
            <onMismatch>DENY</onMismatch>
        </filter>
    </appender>

    <!-- 文件日志1：INFO级别及以上 -->
    <appender name="FILE_INFO2" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>${LOG_PATH}/info2.log</file>
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <fileNamePattern>${LOG_PATH}/info2.%d{yyyy-MM-dd}.log</fileNamePattern>
            <maxHistory>30</maxHistory>
        </rollingPolicy>
        <encoder>
            <pattern>%d{yyyy-MM-dd HH:mm:ss} %-5level [%thread] %logger{36} - %msg%n</pattern>
        </encoder>
        <filter class="ch.qos.logback.classic.filter.LevelFilter">
            <level>INFO</level>
            <onMatch>ACCEPT</onMatch>
            <onMismatch>DENY</onMismatch>
        </filter>
    </appender>

    <!-- 文件日志2：ERROR级别 -->
    <appender name="FILE_ERROR" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>${LOG_PATH}/error.log</file>
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <fileNamePattern>${LOG_PATH}/error.%d{yyyy-MM-dd}.log</fileNamePattern>
            <maxHistory>30</maxHistory>
        </rollingPolicy>
        <encoder>
            <pattern>%d{yyyy-MM-dd HH:mm:ss} %-5level [%thread] %logger{36} - %msg%n</pattern>
        </encoder>
        <filter class="ch.qos.logback.classic.filter.LevelFilter">
            <level>ERROR</level>
            <onMatch>ACCEPT</onMatch>
            <onMismatch>DENY</onMismatch>
        </filter>
    </appender>

    <!-- 根日志记录器 -->
    <root level="INFO">
        <appender-ref ref="CONSOLE" />
        <appender-ref ref="FILE_INFO" />
        <appender-ref ref="FILE_ERROR" />
    </root>

    <!-- 指定某些包或类的日志级别和输出 -->
    <logger name="org.example.hello.springboot" level="DEBUG" additivity="false">
        <appender-ref ref="FILE_INFO" />
        <appender-ref ref="FILE_INFO2" />
        <appender-ref ref="CONSOLE" />
    </logger>
</configuration>

```


## 调度

- 在启动类上加上@EnableScheduling开启定时任务
- 在启动类上加上@EnableScheduling开启定时任务

### 多线程调度

1. 增加多线程配置类在config目录下增加SchedulerConfig配置类，

```
public class SchedulerConfig {
    @Bean
    public Executor taskScheduler() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        executor.setCorePoolSize(3);
        executor.setMaxPoolSize(10);
        executor.setQueueCapacity(3);
        executor.initialize();
        return executor;
    }
}
```
设置执行线程池为3，最大线程数为10。

2. 修改SchedulerTask定时任务修改之前定义的SchedulerTask定时任务的类，在方法上增加@Async注解，使得后台任务能够异步执行

```
@EnableAsync // 开启异步事件的支持
@Component
public class SchedulerTask {
    private static final Logger logger = LoggerFactory.getLogger(SchedulerTask.class);
    @Async
    @Scheduled(cron="*/10 * * * * ?")
    public void taskCron() {
        SimpleDateFormat dateFormat = new SimpleDateFormat("HH:mm:ss");
        logger.info("SchedulerTask taskCron 现在时间： " + dateFormat.format(new Date()));
    }

    @Async
    @Scheduled(fixedRate = 5000)
    public void taskFixed() {
        SimpleDateFormat dateFormat = new SimpleDateFormat("HH:mm:ss");
        logger.info("SchedulerTask taskFixed 现在时间： " + dateFormat.format(new Date()));
    }
}
```
定时任务类SechedulerTask增加了@EnableAsync注解，开启了异步事件支持。同时，在定时方法上增加@Async注解，使任务能够异步执行，这样各个后台任务就不会阻塞。


## IO
### Calling REST Services
#### [RestTemplate](https://docs.spring.io/spring-boot/docs/2.7.18/reference/html/io.html#io.rest-client)

- 依赖

```
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
                <dependency>
            <groupId>org.apache.httpcomponents</groupId>
            <artifactId>httpclient</artifactId>
            <version>4.5.14</version>
        </dependency>
```

- RestTemplate 实例

```
package org.example.hello.springboot;

import org.springframework.boot.web.client.RestTemplateBuilder;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class MyService {

    private final RestTemplate restTemplate;

    public MyService(RestTemplateBuilder restTemplateBuilder) {
        this.restTemplate = restTemplateBuilder.build();
    }

    public String hello() {
        ResponseEntity<Detail> entity = this.restTemplate.getForEntity("http://localhost:8081/api/base/hello", Detail.class);
        Detail re = entity.getBody();
        return re.toString();
    }
}

```