db.createUser({user:"root",pwd:"123456",roles:["root"]})


db.auth("root","xxxx")


## client

```
version: '3.7'

services:
    mongo-express:
      image: mongo-express
      restart: always
      container_name: mongo-express
      ports:
        - "90:8081"
      environment:
        ME_CONFIG_MONGODB_SERVER: root:123456@192.168.3.205
      privileged: true
```