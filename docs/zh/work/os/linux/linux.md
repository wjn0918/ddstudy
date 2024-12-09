---
title: 通用
icon: lightbulb
---


# 查看pid详细信息

Linux在启动一个进程时，系统会在/proc下创建一个以PID命名的文件夹，在该文件夹下会有我们的进程的信息，其中包括一个名为exe的文件即记录了绝对路径，通过ll或ls –l命令即可查看

cwd符号链接的是进程运行目录；

exe符号连接就是执行程序的绝对路径；

cmdline就是程序运行时输入的命令行命令；

environ记录了进程运行时的环境变量；

fd目录下是进程打开或使用的文件的符号连接



# wget
wget http://120.26.77.177:11000/jz2.0/ --recursive --no-parent --http-user=admin --http-passwd=Shingi@2023

--recursive --no-parent 递归下载目录所有

# 进程监控

cesi supervisor 



# cd pushd popd dirs

pushd /home
dirs -p -v

-p 参数可以每行一个目录的形式显示堆栈中的目录列表
-v 参数可以在目录前加上编号
-c 清空目录堆栈

pushd 不加参数 在最近的两个目录之间切换

在多个目录之间切换
pushd +n

popd 


pushd：切换到作为参数的目录，并把原目录和当前目录压入到一个虚拟的堆栈中
                 如果不指定参数，则会回到前一个目录，并把堆栈中最近的两个目录作交换
popd： 弹出堆栈中最近的目录
dirs: 列出当前堆栈中保存的目录列表


# 文件权限
4 -r
2 -w
1 -x

文件类型-用户-其他用户-组


# 添加组

usermod -G groupName userName


# 查看压缩包内容

tar --exclude='*/*/*' -tf packages/grafana-enterprise-10.3.1.linux-amd64.tar.gz