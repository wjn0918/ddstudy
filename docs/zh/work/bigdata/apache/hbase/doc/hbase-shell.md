https://blog.csdn.net/wangqinyi574110/article/details/118424396
https://zhuanlan.zhihu.com/p/117297629


# get

get 


show_filter


scan '表名'， {FILTER =>"过滤器(比较运算符,'比较器')"}



scan 't_cs', {FORMATTER=>'toString'}



# RowFilter
行键过滤器
查询hbase:meta表中rowkey中包含123的数据。

scan 'hbase:meta', {FILTER=> "RowFilter(=,'substring:123')"}


# ValueFilter


值过滤器
查询hbase:meta表中值包含123的数据，因为hbase在存储的时候是以key-value格式的列式存储，在查询遍历的时候每行每列都会遍历,所以才有这个过滤器.
除了可以查询等于，也可以查询大于、大于等于、小于、小于等于、不等于，比较的方式是字典排序。
除非在数据存储的时候存储的类型为数字类型。
substring:包含的意思、binary:精确查询、regexstring:正则匹配、null:空值比较、long:数字比较

scan 'hbase:meta',{FILTER=> "ValueFilter(=，'substring:123')"}


# demo


scan 'ods_hik_zdrysbsj',{FILTER=>"ValueFilter(=, 'substring:方增添')", FORMATTER=>'toString'}
scan 'ods_hik_zdrysbsj',{FILTER=>"ValueFilter(=, 'regexstring:.*袁湘磊.*2023-12-28.*')", FORMATTER=>'toString'}

scan 'ods_hik_zdrysbsj', {FILTER => "FilterList( MUST_PASS_ALL, ValueFilter(=, 'substring:袁湘磊'), ValueFilter(=, 'substring:2023-12-28') )"}
