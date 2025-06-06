---
title: Stock
---
<Catalog/>

## 投资策略


先按pe-ttm  排名  ，然后按pb 排名  将两个排名相加作为综合排名

### Z-Score 优化

```
import pandas as pd

# 示例数据
df = pd.DataFrame({
    'stock': ['A', 'B', 'C', 'D', 'E'],
    'pe_ttm': [10, 15, 8, 20, 12],
    'pb': [1.5, 2.0, 1.0, 3.5, 1.8]
})

# 计算 Z-Score
df['pe_z'] = (df['pe_ttm'] - df['pe_ttm'].mean()) / df['pe_ttm'].std()
df['pb_z'] = (df['pb'] - df['pb'].mean()) / df['pb'].std()

# 低估值更好，因此取负
df['score'] = -df['pe_z'] - df['pb_z']

# 排序，分数越高表示越低估
df = df.sort_values(by='score', ascending=False)

# 选前3只股票
selected = df.head(3)

print(selected[['stock', 'score']])

```


## 参考

https://gitee.com/wjn0918/mop.git

docker run -it --name mop1 registry.cn-hangzhou.aliyuncs.com/wjn0918/soft:mop60015


上证

s_sh


深证

s_sz

## 量化交易

资本资产定价模型（Capital Assset Pricing Model, CAPM）: 重要组成贝塔系数，用于表示某项资产的系统性风险

pandas-datareader