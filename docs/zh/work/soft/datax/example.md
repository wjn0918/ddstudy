---
title: 案例
---

## stream2other
::: tabs
@tab stream

```
{
    "job": {
      "content": [
        {
          "reader": {
            "name": "streamreader",
            "parameter": {
              "sliceRecordCount": 10,
              "column": [
                {
                  "type": "long",
                  "value": "10"
                },
                {
                  "type": "string",
                  "value": "hello，你好，世界-DataX"
                }
              ]
            }
          },
          "writer": {
            "name": "streamwriter",
            "parameter": {
              "encoding": "UTF-8",
              "print": true
            }
          }
        }
      ],
      "setting": {
        "speed": {
          "channel": 5
         }
      }
    }
  }

```

::: 

## mysql2other

::: tabs

@tab stream

```
{
    "job": {
      "content": [
        {
          "reader": {
            "name": "mysqlreader",
            "parameter": {
                "username": "root",
                "password": "123456",
                "column": [
                    "dt_year",
                    "user_name"
                ],
                "connection": [
                    {
                        "table": [
                            "t_1"
                        ],
                        "jdbcUrl": [
"jdbc:mysql://192.168.3.85:3307/cs?useSSL=false"
                        ]
                    }
                ]
            }
          },
          "writer": {
            "name": "streamwriter",
            "parameter": {
              "encoding": "UTF-8",
              "print": true
            }
          }
        }
      ],
      "setting": {
        "speed": {
          "channel": 5
         }
      }
    }
  }
```

@tab hdfs

```
{
    "job": {
      "content": [
        {
          "reader": {
            "name": "mysqlreader",
            "parameter": {
                "username": "root",
                "password": "123456",
                "column": [
                    "dt_year",
                    "user_name"
                ],
                "connection": [
                    {
                        "table": [
                            "t_1"
                        ],
                        "jdbcUrl": [
"jdbc:mysql://192.168.3.85:3307/cs?useSSL=false"
                        ]
                    }
                ]
            }
          },
          "writer": {
            "name": "hdfswriter",
            "parameter": {
                "defaultFS": "hdfs://localhost:9000",
                "fileType": "orc",
                "path": "/tmp/datax/mysqlreader",
                "fileName": "demo",
                "column": [
                    {
                        "name": "dt_year",
                        "type": "VARCHAR"
                    },
                    {
                        "name": "user_name",
                        "type": "VARCHAR"
                    }
                ],
                "writeMode": "append",
                "fieldDelimiter": "\t",
                "compress":"NONE"
            }
          }
        }
      ],
      "setting": {
        "speed": {
          "channel": 5
         }
      }
    }
  }
```

@tab:active hive_partition

```
{
    "job": {
      "content": [
        {
          "reader": {
            "name": "mysqlreader",
            "parameter": {
                "username": "root",
                "password": "123456",
                "column": [
                    "dt_year",
                    "user_name",
                    "score",
                    "director_add_time",
                    "manager_add_time"
                ],
                "connection": [
                    {
                        "table": [
                            "t_1"
                        ],
                        "jdbcUrl": [
"jdbc:mysql://192.168.3.85:3307/cs?useSSL=false"
                        ]
                    }
                ]
            }
          },
          "writer": {
            "name": "hdfswriter",
            "parameter": {
                "defaultFS": "hdfs://localhost:9000",
                "fileType": "orc",
                "path": "/user/hive/warehouse/t_1/dt=20230531",
                "fileName": "demo",
                "column": [
                    {
                        "name": "dt_year",
                        "type": "VARCHAR"
                    },
                    {
                        "name": "user_name",
                        "type": "VARCHAR"
                    },
                    {
                      "name": "score",
                      "type": "int"
                    },
                    {
                      "name": "director_add_time",
                      "type": "VARCHAR"
                    },
                    {
                      "name": "manager_add_time",
                      "type": "VARCHAR"
                    }
                ],
                "writeMode": "append",
                "fieldDelimiter": "\t",
                "compress":"NONE"
            }
          }
        }
      ],
      "setting": {
        "speed": {
          "channel": 5
         }
      }
    }
  }
```

:::