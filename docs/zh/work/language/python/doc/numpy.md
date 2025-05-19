---
title: numpy
---


## case when 

```
df['flag'] = np.where((df['xn'] == '(3+2)') & (df['nj'] == '4'), 1, 0)

result = np.where(arr<=3, 0, np.where(arr<=6, 1, 2))
```