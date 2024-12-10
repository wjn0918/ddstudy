* too many connections

```
systemctl stop mysqld

show variables like "max_connections";
set global max_connections=1000;
```