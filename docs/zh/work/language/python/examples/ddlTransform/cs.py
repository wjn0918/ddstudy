from trans.mysql2hive import convert

# 示例用法
mysql_ddl = """
CREATE TABLE `t_1` (
  `dt_year` year(4) DEFAULT NULL,
  `user_name` varchar(45) DEFAULT NULL,
  `score` int(11) DEFAULT NULL,
  `director_add_time` int(11) unsigned DEFAULT '0' COMMENT '升级为主任的时间',
  `manager_add_time` int(11) unsigned DEFAULT '0' COMMENT '升级为经理的时间'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""

hive_ddl = convert(mysql_ddl)
print(hive_ddl)
