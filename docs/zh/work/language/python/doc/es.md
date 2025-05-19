---
title: es
---

```

def get_instance_data(es_index, columns):
    """
    es_index: es索引
    columns: es字段映射
    获取模型实例数据
    """
    es = Elasticsearch(hosts="10.45.192.180",port=9201,timeout=3600)
    body = {"query": {"match_all": {}}}
    query = es.search(index=es_index, body=body,scroll='5m',size=100)
    
    
    results = query['hits']['hits'] # es查询出的结果第一页
    total = query['hits']['total']['value']  # es查询出的结果总量
    scroll_id = query['_scroll_id'] # 游标用于输出es查询出的所有结果
    for i in range(0, int(total/100)+1):
        # scroll参数必须指定否则会报错
        query_scroll = es.scroll(scroll_id=scroll_id,scroll='5m')['hits']['hits']
        results += query_scroll
    instance_data = [i['_source'] for i in results]
    df = pd.DataFrame(instance_data)
    df = df.rename(columns=columns)
    return df

```