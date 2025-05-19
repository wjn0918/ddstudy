---
title: code-server
---

## 后台启动

```
screen -S mycodeserevr
```

```
code-server
```

```
Ctrl+D  # 在当前screen下，输入Ctrl+D，删除该screen
Ctrl+A，Ctrl+D  # 在当前screen下，输入先后Ctrl+A，Ctrl+D，退出该screen

```

- 查看

```
screen -ls
```

- 删除
```
screen -X -S  id quit
```