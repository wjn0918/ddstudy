---
title: SqlAlchemy
---

## [Engine](https://docs.sqlalchemy.org/en/20/core/engines.html)

::: tabs

@tab Pgsql

```
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:tiger@localhost:5432/mydatabase")
```

:::


## 特殊字符

```
from sqlalchemy import URL
from sqlalchemy import create_engine

url_object = URL.create(
    "postgresql+pg8000",
    username="dbuser",
    password="kx@jj5/g",  # plain (unescaped) text
    host="pghost10",
    database="appdb",
)

engine = create_engine(url_object)
```