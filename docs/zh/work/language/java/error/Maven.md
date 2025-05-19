---
title: Maven
---




* sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target 

Maven 在解析和下载依赖时遇到了 SSL 证书验证问题

可以在 Maven 命令行添加 -Dmaven.wagon.http.ssl.insecure=true 参数来跳过 SSL 验证


连接超时
-Dhttp.connectionTimeout=60000 -Dhttp.socketTimeout=60000