---
title: Flask
---
## migrate

> pip install Flask-Migrate -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

```
flask db init
flask db migrate -m 'init'
flask db upgrade

```



* No such command 'db'.

需要添加

```
migrate = Migrate(app, db)
```




## powershell

cd app
$env:FLASK_APP="app.py"
flask run



