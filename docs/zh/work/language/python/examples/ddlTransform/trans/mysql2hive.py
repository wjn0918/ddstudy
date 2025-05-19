import re


def map_data_type():
    """
    将MySQL数据类型转换为对应的Hive数据类型
    :return:
    """
    data_type_mapping = {
        'year': 'int',
        'varchar': 'string',
        'int': 'int',
        # 添加其他数据类型的映射规则
    }
    return data_type_mapping


def convert(mysql_ddl):
    # 去除换行符和注释
    ddl = re.sub(r'\s+', ' ', mysql_ddl)
    ddl = re.sub(r'/\*.*?\*/', '', ddl)

    # 替换MySQL特定语法为Hive语法
    ddl = ddl.replace('`', '')  # 去除MySQL的反引号

    # 将MySQL数据类型转换为对应的Hive数据类型
    data_type_mapping = map_data_type()

    for data_type, hive_data_type in data_type_mapping.items():
        ddl = re.sub(fr'{data_type}\(\d+\)', hive_data_type, ddl)

    # 移除默认值
    ddl = re.sub(r'DEFAULT\s+[^,\s]+', '', ddl)

    # 添加Hive特定语法
    ddl = ddl.replace('ENGINE=InnoDB', '')
    ddl = ddl.replace('DEFAULT CHARSET=utf8', '')
    ddl = ddl.replace('unsigned', '')

    return ddl.strip() + r"""
    PARTITIONED BY (dt string)
    ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
    STORED AS ORC;
    """
