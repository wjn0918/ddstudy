import pandas as pd 
from sqlalchemy import create_engine
from urllib.parse import quote_plus as urlquote
password = urlquote("Mysql@2023")

engine = create_engine(f"mysql+mysqldb://root:{password}@192.168.3.204:3306/zjioc_202?charset=utf8")

with engine.connect() as conn, conn.begin():
    # 模型
    model = pd.read_sql("select * from dp_dorm limit 10", conn)

model