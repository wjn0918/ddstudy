---
title: FastAPI
---


```
my_fastapi_project/
│
├── app/
│   ├── core/                    # 核心配置，如数据库、安全等
│   │   ├── __init__.py
│   │   ├── config.py            # 配置文件
│   │   └── security.py          # 安全相关设置（例如JWT认证）
│   │
│   ├── dependencies/            # 依赖注入
│   │   ├── __init__.py
│   │   └── some_dependency.py   # 自定义依赖
│   │
│   ├── models/                  # 数据库模型
│   │   ├── __init__.py
│   │   └── user.py              # 用户模型示例
│   │
│   ├── routers/                 # 路由分组
│   │   ├── __init__.py
│   │   ├── users.py             # 用户相关的路由
│   │   └── items.py             # 物品相关的路由
│   │
│   ├── schemas/                 # Pydantic 模型（请求和响应数据格式）
│   │   ├── __init__.py
│   │   ├── user.py              # 用户Pydantic模型
│   │   └── item.py              # 物品Pydantic模型
│   │
│   ├── services/                # 业务逻辑层
│   │   ├── __init__.py
│   │   ├── user_service.py      # 用户服务层实现
│   │   └── item_service.py      # 物品服务层实现
│   │
│   ├── utils/                   # 工具函数或类
│   │   ├── __init__.py
│   │   └── helper_functions.py  # 帮助函数
│   │
│   ├── main.py                  # 主应用入口
│   └── database.py              # 数据库连接和初始化
│
├── tests/                        # 测试用例
│   ├── __init__.py
│   ├── test_users.py            # 用户模块测试
│   └── test_items.py            # 物品模块测试
│
├── .env                          # 环境变量文件
├── requirements.txt              # Python依赖包列表
└── README.md                     # 项目说明文档

```

## 接收文件

```
from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
import uvicorn

app = FastAPI()

@app.put("/{filename}")
async def upload_file(filename: str, request: Request):
    with open(filename, "wb") as f:
        f.write(await request.body())
    return PlainTextResponse(f"Saved as {filename}\n")

```

### 使用curl 进行传输

```
curl --upload-file /etc/passwd http://ip:port/passwd.txt
```

```
for file in $(find /home/wjn/soft -type f); do
  echo "Uploading $file"
  curl --upload-file "$file" "http://ip:port/$(basename "$file")"
done


```


### 启动脚本

```
#!/bin/bash

# 定义变量
APP="main:app"
PORT=5001
PID_FILE="uvicorn.pid"
LOG_FILE="uvicorn.log"

# 启动 Uvicorn 服务
start() {
    if [ -f "$PID_FILE" ]; then
        echo "Uvicorn 已经在运行 (PID: $(cat $PID_FILE))"
        exit 1
    fi

    echo "正在启动 Uvicorn (端口: $PORT)..."
    nohup uvicorn $APP --port=$PORT > $LOG_FILE 2>&1 &
    echo $! > $PID_FILE
    echo "Uvicorn 已启动 (PID: $(cat $PID_FILE))"
}

# 停止 Uvicorn 服务
stop() {
    if [ ! -f "$PID_FILE" ]; then
        echo "Uvicorn 未运行"
        exit 1
    fi

    PID=$(cat $PID_FILE)
    echo "正在停止 Uvicorn (PID: $PID)..."
    kill -9 $PID
    rm $PID_FILE
    echo "Uvicorn 已停止"
}

# 查看状态
status() {
    if [ -f "$PID_FILE" ]; then
        PID=$(cat $PID_FILE)
        if ps -p $PID > /dev/null; then
            echo "Uvicorn 正在运行 (PID: $PID)"
        else
            echo "Uvicorn PID 文件存在但进程未运行"
        fi
    else
        echo "Uvicorn 未运行"
    fi
}

# 主逻辑
case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart)
        stop
        start
        ;;
    status)
        status
        ;;
    *)
        echo "使用方法: $0 {start|stop|restart|status}"
        exit 1
esac

exit 0
```