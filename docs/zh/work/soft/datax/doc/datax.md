# hdfswriter

truncate  清空数据


# 

java -server -Xms1g -Xmx1g -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/home/hadoop/soft/datax/log -Xms1g -Xmx1g -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/home/hadoop/soft/datax/log -Dloglevel=info -Dfile.encoding=UTF-8 -Dlogback.statusListenerClass=ch.qos.logback.core.status.NopStatusListener -Djava.security.egd=file:///dev/urandom -Ddatax.home=/home/hadoop/soft/datax -Dlogback.configurationFile=/home/hadoop/soft/datax/conf/logback.xml -classpath /home/hadoop/soft/datax/lib/*:.  -Dlog.file.name=ft_datax_job_cs_json com.alibaba.datax.core.Engine -mode standalone -jobid -1 -job /home/hadoop/soft/datax/job/cs.json



# 编译

*  Could not find goal 'assembly' in plugin org.apache.maven.plugins:maven-assembly-plugin:3.4.2 among available goals help, single

maven-assembly-plugin 设置版本
<artifactId>maven-assembly-plugin</artifactId>
<version>2.2-beta-5</version>




当提升DataX Job内Channel并发数时，调整JVM heap参数，原因如下：
         - 当一个Job内Channel数变多后，内存的占用会显著增加，因为DataX作为数据交换通道，在内存中会缓存较多的数据。
         - 例如Channel中会有一个Buffer，作为临时的数据交换的缓冲区，而在部分Reader和Writer的中，也会存在一些Buffer，为了防止jvm报内存溢出等错误，调大jvm的堆参数。
         - 通常我们建议将内存设置为4G或者8G，这个也可以根据实际情况来调整
         - 调整JVM xms xmx参数的两种方式：一种是直接更改datax.py；另一种是在启动的时候，加上对应的参数，如下： 
           python datax/bin/datax.py --jvm="-Xms8G -Xmx8G" XXX.json
Channel个数并不是越多越好， 原因如下：
           - Channel个数的增加，带来的是更多的CPU消耗以及内存消耗。
           - 如果Channel并发配置过高导致JVM内存不够用，会出现的情况是发生频繁的Full GC，导出速度会骤降，适得其反。这个可以通过观察日志发现








```
public class HikApiReader extends Reader {
    public static class Job extends Reader.Job {
        @Override
        public List<Configuration> split(int adviceNumber) {
            List<Configuration> readerSplitConfigs = new ArrayList<>();
            
            int totalPageCount = calculateTotalPageCount(); // 计算总页数
            
            // 根据建议的并行度和总页数均匀分配配置
            int pagesPerTask = totalPageCount / adviceNumber;
            int remainingPages = totalPageCount % adviceNumber;
            
            for (int i = 0; i < adviceNumber; i++) {
                Configuration taskConfig = getTaskConfig().clone();
                
                // 计算当前任务处理的页数范围
                int startIndex = i * pagesPerTask + Math.min(i, remainingPages);
                int endIndex = startIndex + pagesPerTask + (i < remainingPages ? 1 : 0);
                
                taskConfig.set("startIndex", startIndex);
                taskConfig.set("endIndex", endIndex);
                
                readerSplitConfigs.add(taskConfig);
            }
            
            return readerSplitConfigs;
        }
    }

    public static class Task extends Reader.Task {
        private Configuration readerSliceConfig = null;
        private int startIndex;
        private int endIndex;

        @Override
        public void init() {
            this.readerSliceConfig = this.getPluginJobConf();
            this.startIndex = this.readerSliceConfig.getInt("startIndex");
            this.endIndex = this.readerSliceConfig.getInt("endIndex");
        }

        @Override
        public void startRead(RecordSender recordSender) {
            for (int i = startIndex; i < endIndex; i++) {
                String body = buildRequestBodyForPage(i);
                doRead(recordSender, body);
            }
        }
        
        // 其他方法和代码保持不变
    }
}

```