---
title: pandas
---

## 重命名列

df.rename(columns={'A': 'a', 'B': 'b'}, inplace=True)

## 更改数据格式

 df.astype(str)


# 随机数

data['B_repair_score'] = np.random.randint(0, 30, size=n)

# 排序

df_sorted = df_filtered.sort_values(by='asset_score', ascending=True)


# mysql

```
import pandas as pd 
from sqlalchemy import create_engine

import urllib.parse
urllib.parse.quote_plus("kx@jj5/g")

engine = create_engine("mysql+mysqldb://mwdevsql:Dev20$uiyD7@192.168.3.22/monitor?charset=utf8")

with engine.connect() as conn, conn.begin():
    data = pd.read_sql_table("mw_cmdbmd_manage", conn)
data

```


# How to Calculate a Difference Between Two Dates

天

> df['diff_days'] = (df['end_date'] - df['start_date']) / np.timedelta64(1, 'D')

年/月

(df_asset['today'].dt.to_period('Y')
                       .sub(df_asset['start_date'].dt.to_period('Y'))
                       .apply(lambda x: x.n)
                      )



# in / not in

Series.isin(['1','2'])

~Series.isin(['1','2'])


# group by apply 后取group by 字段

def cs(item:pd.DataFrame):
    group_by = item.name


# group by 

df.groupby('资产管理类别名称').apply(lambda data: data['数量'].sum(), include_groups=False)

# group by 多列

```

import pandas as pd

# 创建示例数据
data = {
    '部门': ['销售', '销售', '财务', '财务', '技术'],
    '城市': ['北京', '上海', '北京', '上海', '北京'],
    '销售额': [100, 200, 150, 180, 120]
}

df = pd.DataFrame(data)

# 对部门和城市进行分组，并计算销售额的总和
grouped = df.groupby(['部门', '城市']).sum()

# 输出结果
print(grouped)
```

# apply 返回多列

r[['column1', 'column2']] = df.apply(lambda x: cs(x)).to_list()

# case_when 2.2.0

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(10).reshape(10,1), columns=['id'])
df['cs'] = "Unknown"
df['cs'].case_when([
    (df.eval("id < 3"),10),
    (df.eval("3 <= id < 6"), 20),
    (df.eval(" id >= 6"), 30)
    
    ]
)
```


# 根据某列生成重复数据

```
import pandas as pd
from itertools import product

# 原始DataFrame
df = pd.DataFrame({
    'use_y': [1, 2, 3],
    'col1': ['a', 'b', 'c'],
    'col2': [10, 20, 30]
})

# 定义函数，但这次返回合并后的DataFrame
def cs(row: pd.Series):
    # 创建一个空DataFrame用来存放结果
    result = pd.DataFrame()
    
    for _ in range(row['use_y']): 
        temp = pd.DataFrame(row[['col1', 'col2']].to_dict(), index=[0])
        result = pd.concat([result, temp])
    return result

# 应用函数并将结果融合成一个大的DataFrame
df2 = pd.concat(df.apply(cs, axis=1).tolist())

# 如果需要重置索引
df2.reset_index(drop=True, inplace=True)

print(df2)

```