---
title: 配置
---

## ZEPPELIN_INTERPRETER_OUTPUT_LIMIT

更改zeppelin.interpreter.output.limit


## [分享段落](https://zeppelin.apache.org/docs/latest/usage/other_features/publishing_paragraphs.html)

## iframe 无法被嵌入

修改  zeppelin-site.xml  zeppelin.server.xframe.options
```
add_header X-Frame-Options SAMEORIGIN;
（1）DENY：不能被嵌入到任何iframe或frame中。

（2）SAMEORIGIN：页面只能被本站页面嵌入到iframe或者frame中。

（3）ALLOW-FROM uri：只能被嵌入到指定域名的框架中。

（4）AllowAll：允许所有站点内嵌。
```


## dataframe 转为table
```
%python
import pandas as pd



def convert_to_table(data):
    row_content = ""
    for index,col in enumerate(columns):
        if index==0:
            row_content += f"{data[col]}"
        else:
            row_content += f"\t{data[col]}"
    return row_content

    

df = pd.DataFrame({"a":[1,2,3],"b":[1,2,3]})

columns = df.columns.tolist()
rows = df.shape[0]


df['content'] = df.apply(lambda data:convert_to_table(data), axis=1)
# df[['content']].apply(lambda data:convert_row(data), axis=0)

columns_name = "\t".join(columns)

r = "\n".join(df['content'].tolist())

print(f"""%table
{columns_name}
{r}
""")

```