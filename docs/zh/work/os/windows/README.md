---
title: Windows
---


## 启用管理员

```
net user administrator /active:yes

```

## 环境变量


* 使用setx命令可以为当前用户设置环境变量。这个变量只对当前用户有效。
```
setx MY_VARIABLE "my value"
```

* 若要设置系统级别的环境变量（即对所有用户都有效），需要加上/M参数：

```
setx MY_VARIABLE "my value" /M
```

重启应用后使用echo %MY_VARIABLE%（CMD）或echo $env:MY_VARIABLE（PowerShell）来验证


## [tree](https://learn.microsoft.com/zh-cn/windows-server/administration/windows-commands/tree)
以图形方式显示路径或驱动器中磁盘的目录结构

目前无法输出隐藏文件


```
tree [<drive>:][<path>] [/f] [/a]
```


