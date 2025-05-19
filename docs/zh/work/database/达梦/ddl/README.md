<!--
 * @Author: wjn
 * @Date: 2020-11-12 09:32:51
 * @LastEditors: wjn
 * @LastEditTime: 2021-06-17 10:24:15
-->


alter user "" identified by "123"




2) 创建表空间和用户
create tablespace "zfw" datafile 'TEST01.DBF' size 2048 autoextend on next 2048, 'TEST02.DBF' size 2048 autoextend on next 2048;
 
--建议每个用户单独规划一个表空间,便于单独管理
--根据数据量,每个表空间规划多个数据文件,分散io压力
 
CREATE USER TEST IDENTIFIED BY "TEST123456" DEFAULT TABLESPACE TEST;
GRANT DBA TO TEST;       --赋予dba权限
GRANT RESOURCE TO TEST;  --赋予普通权限



function createDb(ms,mm){
    var t = `
    create tablespace "{MS}" datafile '{MS}01.DBF' size 2048 autoextend on next 2048, '{MS}02.DBF' size 2048 autoextend on next 2048;
 
--建议每个用户单独规划一个表空间,便于单独管理
--根据数据量,每个表空间规划多个数据文件,分散io压力
 
CREATE USER {MS} IDENTIFIED BY "{MM}" DEFAULT TABLESPACE {MS};
GRANT DBA TO {MS};       --赋予dba权限
GRANT RESOURCE TO {MS};  --赋予普通权限
    `;
    return t.replace(/{MS}/g,ms).replace(/{MM}/g,mm)
}
createDb('ZFW_WW_SY','ZFW_WW_SY') 







1）查询表空间下的表

select * from all_tab_comments where owner='表空间名' order by TABLE_NAME asc

2）查询表的字段

SELECT  T1.COLUMN_NAME,T1.DATA_TYPE,T1.DATA_LENGTH,T2.COMMENTS
FROM ALL_TAB_COLUMNS T1
LEFT JOIN ALL_COL_COMMENTS T2
ON  (T1.TABLE_NAME= T2.TABLE_NAME AND T1.COLUMN_NAME= T2.COLUMN_NAME)
WHERE T1.TABLE_NAME='表名'
AND T1.OWNER='表空间名'
AND T2.OWNER='表空间名'


# 修改用户密码
alter user test1 identified by "test123456";