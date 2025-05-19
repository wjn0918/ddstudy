---
title: 案例
---


## warning

pgsql 字段存在大小写需要配置成

```
"\"workspaceId\""
```


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

@tab pgsql

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
          "name": "postgresqlwriter",
          "parameter": {
            "username": "postgres",
            "password": "Pgsql@2024",
            "column": [
              "dorm_access_record_id",
              "workspace_id",
              "user_id",
              "name",
              "job_no",
              "gender",
              "face_photo",
              "depart_id",
              "depart_name",
              "major_id",
              "major",
              "college_id",
              "college_name",
              "dorm_building_id",
              "building_name",
              "equipment_id",
              "equipment_name",
              "access_type",
              "access_time",
              "access_photo",
              "created_at",
              "created_by",
              "created_by_account",
              "updated_at",
              "updated_by",
              "updated_by_account",
              "deleted",
              "created_by_name",
              "updated_by_name",
              "identity_card"

            ]
          ,
            "preSql": [

            ],
            "connection": [
              {
                "jdbcUrl": "jdbc:postgresql://192.168.3.205:5432/park-preview",
                "table": [
                  "t_dorm_access_record"
                ]
              }
            ]
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

## pgsql2other

::: tabs

@tab pgsql

```
{
    "job": {
      "content": [
        {
          "reader": {
            "name": "postgresqlreader",
            "parameter": {
                "username": "postgres",
                "password": "Pgsql@2024",
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
                          "jdbc:postgresql://172.31.24.131:5432/postgres"
                        ]
                    }
                ]
            }
          },
          "writer": {
          "name": "postgresqlwriter",
          "parameter": {
            "username": "postgres",
            "password": "Pgsql@2024",
            "column": [
              "dorm_access_record_id",
              "workspace_id",
              "user_id",
              "name",
              "job_no",
              "gender",
              "face_photo",
              "depart_id",
              "depart_name",
              "major_id",
              "major",
              "college_id",
              "college_name",
              "dorm_building_id",
              "building_name",
              "equipment_id",
              "equipment_name",
              "access_type",
              "access_time",
              "access_photo",
              "created_at",
              "created_by",
              "created_by_account",
              "updated_at",
              "updated_by",
              "updated_by_account",
              "deleted",
              "created_by_name",
              "updated_by_name",
              "identity_card"

            ]
          ,
            "preSql": [

            ],
            "connection": [
              {
                "jdbcUrl": "jdbc:postgresql://192.168.3.205:5432/park-preview",
                "table": [
                  "t_dorm_access_record"
                ]
              }
            ]
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