Dockerfile
```
FROM node:18-alpine3.15

COPY ./packages /company-web

WORKDIR /company-web

RUN npm install

CMD ["node", "app.js"]
```

# Dockerfile
```
FROM node:18-alpine3.15
COPY ./ /app
WORKDIR /app
CMD ["sh", "run.sh"]

```

# run.sh

```
#!/bin/bash

npm start

tail -f /dev/null
```