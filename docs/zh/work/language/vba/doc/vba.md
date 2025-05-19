# 注释

' 注释文本

# 输出

Debug.Print "hello"

# 数组

dim 数组名() as 数据类型

数组名(0) = 数据

debug.print join(数组名, "分隔符")


# for

```
For Each i In data
    Debug.Print i  ' debug
Next



' 按行或列处理

For Each i In Selection.columns
    For Each j In i.Rows
        Debug.Print "----"; j.Value
    Next j
Next i

```


# 查看属性

debug.print typename(i)


# range 转数组

如果取的range是1列，那么transpose1次可以变成1维数组
如果取的range是1行，那么transpose2次可以变成1维数组


'单列
arr1 = Range("a1:a10")
'单行
arr2 = Range("a1:e1")
arr11 = Application.Transpose(arr1)
arr21 = Application.Transpose(Application.Transpose(arr2))


 
Debug.Print "用for index 的方法遍历"
For I = LBound(arr1) To UBound(arr1)
    Debug.Print arr1(I, 1)
Next



# 换行
chr(9)  -- tab
chr(10)  -- 换行符
chr(13)  -- 回车符
vbcrlf -- 换行+回车



Sub cs2()

Dim data As Variant
data = Range("A1:A10").Value
For Each i In data
    Debug.Print i  ' debug
Next


End Sub
