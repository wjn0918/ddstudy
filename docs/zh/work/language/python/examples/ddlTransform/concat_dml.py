import pandas as pd
from pandas import DataFrame
import numpy as np


class DatabaseTable:
    def __init__(self, table_name, table_comment, fields=[], target_fields=[], where=None, where_comment=None, left_join=None, left_join_comment=None):
        self.table_name = table_name
        self.table_comment = table_comment
        self.fields = fields
        self.target_fields = target_fields
        self.table_alias = None  # 默认情况下表别名为空
        self.where = where if where else []  # 初始化查询条件为一个空列表
        self.where_comment = where_comment if where_comment else {}  # 初始化过滤条件说明为一个空字典
        self.left_join = left_join if left_join else []
        self.left_join_comment = left_join_comment if left_join_comment else {}  # 初始化过滤条件说明为一个空字典

    def add_field(self, field_name, field_type, field_comment):
        field = {
            'field_name': field_name,
            'field_type': field_type,
            'field_comment': field_comment
        }
        self.fields.append(field)

    def add_target_field(self, field_name, field_type, field_comment):
        field = {
            'field_name': field_name,
            'field_type': field_type,
            'field_comment': field_comment
        }
        self.target_fields.append(field)

    def set_table_alias(self, table_alias):
        self.table_alias = table_alias

    def set_where_clause(self, conditions):
        self.where = conditions

    def set_where_comment(self, comment):
        self.where_comment = comment

    def set_left_join(self, join_clauses):
        self.left_join = join_clauses

    def set_left_join_comment(self, comment):
        self.left_join_comment = comment

    def get_left_join_str(self):
        # Construct left join clause
        left_join_str = [
            f'{condition} -- {self.left_join_comment[condition] if self.left_join_comment.get(condition, "") else ""}'
            for condition in self.left_join
        ]
        return ' \n\tAND '.join(left_join_str)

    def get_columns(self):
        columns_str = [
            f'{self.table_alias}.{field['field_name']} as {self.target_fields[index]['field_name']} -- {self.target_fields[index]['field_comment']}'
            for index,field in enumerate(self.fields)
        ]

        return ' \n\t,'.join(columns_str)



    def __str__(self):
        where_clause = " AND ".join(self.where) if self.where else "None"
        where_comment_info = "\n".join(
            [f"  - {condition}: {comment}" for condition, comment in self.where_comment.items()])
        left_join = " AND ".join(self.left_join) if self.left_join else "None"

        table_info = f"Table Name: {self.table_name}\n" \
                     f"Table Comment: {self.table_comment}\n" \
                     f"Table Alias: {self.table_alias}\n" \
                     f"Where Comment:\n{where_comment_info}\n" \
                     f"Where Clause: {where_clause}\n" \
                     f"left join Clause: {left_join}\n" \
                     "Fields:\n"

        for field in self.fields:
            table_info += f"  - Name: {field['field_name']}, Type: {field['field_type']}, Comment: {field['field_comment']}\n"

        return table_info

    def generate_query(self):
        # Construct SELECT clause
        fields_str_list = [f'{field["field_name"]} -- {field["field_comment"]}' for field in
                           self.fields]
        select_clause = ' \n\t,'.join(fields_str_list)

        # Construct FROM clause
        from_clause = f'FROM {self.table_name}'

        # Construct WHERE clause
        where_str_list = [
            f'{condition} {"--" + self.where_comment[condition] if self.where_comment.get(condition, "") else ""}'
            for condition in self.where
        ]
        where_clause = ' \n\tAND '.join(where_str_list)

        # Combine all parts to form the complete SQL query
        query = f'SELECT \n\t {select_clause}\n{from_clause}\n'
        if where_clause:
            query += f'WHERE \n\t{where_clause}'

        return query

    def generate_hive_with_query(self):
        query = f'{self.table_alias} AS (\n\t--{self.table_comment}\n\t{self.generate_query().replace('\n', '\n\t')}\n)'
        return query


# 创建 DatabaseTable 对象的函数
def create_database_table(group):
    print(group)
    table_name = group['来源表'].iloc[0]
    table_comment = group['来源表备注'].iloc[0]

    table_info = DatabaseTable(table_name, table_comment)
    table_info.fields = []
    table_info.where = []
    table_info.where_comment = {}
    table_info.left_join_comment = {}
    table_info.left_join = []
    where = []
    where_comment = {}
    left_join = []
    left_join_comment= {}
    for _, row in group.iterrows():
        table_info.add_field(row['来源字段'], row['来源字段类型'], row['来源字段备注'])
        table_info.add_target_field(row['字段名称'], row['字段类型'], row['字段备注'])

        if pd.notna(row['where']):
            where.append(row['where'])

        if pd.notna(row['where说明']):
            where_comment[row['where']] = row['where说明']

        if pd.notna(row['left_join']):
            left_join.append(row['left_join'])

        if pd.notna(row['left_join_comment']):
            left_join_comment[row['left_join']] = (row['left_join_comment'])
    table_info.set_where_clause(where)
    table_info.set_where_comment(where_comment)
    table_info.set_left_join(left_join)
    table_info.set_left_join_comment(left_join_comment)
    table_info.set_table_alias(group['来源表别名'].iloc[0])
    return table_info


def create_hive_with_sql(df: DataFrame):
    """
    创建hive with sql
    :param df: pandas dataframe
    :return:
    """
    (table_name, table_comment) = df.iloc[0, 0:2]
    # 创建 DatabaseTable 对象
    table = DatabaseTable(table_name=table_name, table_comment=table_comment)

    fields_df: DataFrame = df.iloc[1:]
    column_names = ['字段名称', '字段类型', '字段备注', '来源表', '来源表备注', '来源表别名', '来源字段',
                    '来源字段类型', '来源字段备注', 'where', 'where说明', 'left_join', 'left_join_comment']
    fields_df.columns = column_names
    print(fields_df)

    # 根据来源表别名分组，创建 DatabaseTable 对象
    database_tables = fields_df.groupby('来源表别名').apply(create_database_table)

    # Assuming database_tables is a list of DatabaseTable objects
    primary_table = database_tables.iloc[0]  # type: DatabaseTable
    subsequent_tables = database_tables.iloc[1:]

    # Generate SQL query for the primary table
    sql_query = f'WITH {primary_table.generate_hive_with_query()}'

    # Append LEFT JOIN clauses for subsequent tables
    for table in subsequent_tables:
        print(table.get_columns())
        sql_query += f',\n{table.generate_hive_with_query()}\n'
    columns = ""
    for index, table in enumerate(database_tables):
        if index > 0:
            columns += f'\n\t,{table.get_columns()}'
        else:
            columns += f'\n\t{table.get_columns()}'
    sql_query += f'SELECT \n{columns}\nFROM \n\t{primary_table.table_alias}'
    for table in subsequent_tables:  # type: DatabaseTable
        sql_query += f'\nLEFT JOIN {table.table_alias} ON \n\t{table.get_left_join_str()}'
    # Print the final SQL query
    print(sql_query)
    print("=" * 50)

if __name__ == "__main__":
    all_df:DataFrame = pd.read_excel(r"表结构.xls", header=None)
    df_list = [group for _, group in all_df.groupby((all_df.isnull().all(1)).cumsum())] # type: list[DataFrame]
    for df in df_list[0:1]:
        print(df)
        df = df.dropna(how='all') # 删除空行
        df = df.dropna(subset=[df.columns[4]])
        create_hive_with_sql(df)
