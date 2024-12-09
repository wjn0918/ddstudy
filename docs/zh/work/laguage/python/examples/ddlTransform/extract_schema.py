from sqlalchemy import Column, String, create_engine, select
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from urllib import parse
import json
import openpyxl as op


Base = declarative_base()
# url = "mysql+pymysql://root:123456@localhost:3306/information_schema?charset=utf8"
url = "mysql+pymysql://root:%s@101.43.104.61:3306/information_schema?charset=utf8" % parse.quote_plus('shingi@123123')
engine = create_engine(url)

tables = [
    "dorm_access_record",
    "pi_access_record",
    "fp_smoke_detector",
    "vehicle_access",
    "vehicle_violation",
    "dorm_check_in",
    "dorm_student_leave",
    "dorm_unoccupied",
    "fp_smoke_equipment",
    "pi_student",
    "pi_teacher",
    "pi_org",
    "sys_dept",
    "sys_user"
]

table_comments = [
    "宿舍进出记录",
    "人员进出记录",
    "感烟火灾探测器",
    "车辆进出记录",
    "车辆违章记录",
    "学生入住信息",
    "学生未入住信息",
    "学生请假记录",
    "无线烟感设备",
    "学生信息",
    "教职工信息",
    "基础信息组织架构",
    "系统组织架构",
    "用户信息"
]


class Schema(Base):
    __tablename__ = 'COLUMNS'

    table_schema = Column(String)
    table_name = Column(String)
    column_name = Column(String)
    column_comment = Column(String)
    column_type = Column(String)

    __mapper_args__ = {
        'primary_key': [table_schema, table_name, column_name, column_comment, column_type]
    }

    # def __repr__(self):
    #     return json.dumps({
    #         "table_schema": self.table_schema,
    #         "table_name": self.table_name,
    #         "column_name": self.column_name,
    #         "column_comment": self.column_comment,
    #         "column_type": self.column_type
    #     })


def get_table_schema(table_name):
    """
    获取表元数据
    :param table_name:
    :return:
    """
    session = Session(engine)
    stmt = select(Schema).where(Schema.table_schema.__eq__("zjioc"),
                                Schema.table_name.__eq__(table_name))
    res = session.scalars(stmt).all()
    return res


def to_excel(table_name, table_comment, out):
    """
    数据输出到excel
    :param out:
    :return:
    """
    op_toexcel(table_name, table_comment, out)
    pass


def op_toexcel(table_name, table_comment, data, filename="demo.xlsx"):
    """
    openpyxl库储存数据到excel
    :param data:
    :param filename:
    :return:
    """
    try:
        wb = op.load_workbook(filename)
        ws = wb['Sheet']  # 创建子表
        ws.append(['','',''])
    except:
        print('重新导出')
        wb = op.Workbook()  # 创建工作簿对象
        ws = wb['Sheet']  # 创建子表

    ws.append([table_name, table_comment, ''])
    ws.append(['字段名','备注','字段类型', '来源表', '来源字段', '来源字段备注', '来源字段类型']) # 添加表头
    for i in range(len(data)):
        r = [data[i].column_name, data[i].column_comment, data[i].column_type]
        ws.append(r) # 每次写入一行
    wb.save(filename)


if __name__ == '__main__':

    print("===========start==========")
    for i, table_name in enumerate(tables):
        print(table_name)
        schemas = get_table_schema(table_name)
        to_excel(table_name, table_comments[i], schemas)
        # print(schemas)
