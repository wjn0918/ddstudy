---
title: 配置
---

## 更改日志级别
```
python bin/datax.py --loglevel debug job/
```


当提升DataX Job内Channel并发数时，调整JVM heap参数，原因如下：
         - 当一个Job内Channel数变多后，内存的占用会显著增加，因为DataX作为数据交换通道，在内存中会缓存较多的数据。
         - 例如Channel中会有一个Buffer，作为临时的数据交换的缓冲区，而在部分Reader和Writer的中，也会存在一些Buffer，为了防止jvm报内存溢出等错误，调大jvm的堆参数。
         - 通常我们建议将内存设置为4G或者8G，这个也可以根据实际情况来调整
         - 调整JVM xms xmx参数的两种方式：一种是直接更改datax.py；另一种是在启动的时候，加上对应的参数，如下： 
           python datax/bin/datax.py --jvm="-Xms8G -Xmx8G" XXX.json
Channel个数并不是越多越好， 原因如下：
           - Channel个数的增加，带来的是更多的CPU消耗以及内存消耗。
           - 如果Channel并发配置过高导致JVM内存不够用，会出现的情况是发生频繁的Full GC，导出速度会骤降，适得其反。这个可以通过观察日志发现
