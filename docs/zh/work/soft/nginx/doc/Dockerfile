FROM nginx:1.24.0
# 设置工作目录，可选
WORKDIR /app

# 将你的 Java 应用程序 JAR 文件添加到容器中
COPY dist/ /app/dist/

# 启动 Nginx
CMD ["nginx", "-g", "daemon off;"]

# mkdir -p school-front/conf.d

