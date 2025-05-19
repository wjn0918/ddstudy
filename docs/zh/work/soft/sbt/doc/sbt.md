* 更改仓库地址

```
# ~/.sbt/1.0/global.sbt


val localRepo = "D:\\repository\\java"
resolvers += Resolver.file("Local Maven Repo", file(localRepo))(Resolver.mavenStylePatterns)

```