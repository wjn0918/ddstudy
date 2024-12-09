# 填充文本
```

Sub FillSelectedRowsBasedOnFourthColumn()
    Dim rng As Range
    Dim cell As Range
    Dim firstRow As Range
    
    ' 获取选中的区域
    Set rng = Selection

    ' 获取选中区域的第一行
    Set firstRow = rng.Rows(1)

    ' 遍历选中的所有行（跳过第一行）
    For Each cell In rng.Columns(4).Cells
        If cell.Row > rng.Rows(1).Row Then
            If Not IsEmpty(cell.Value) Then ' 判断第四列是否有数据
                cell.Offset(0, -3).Value = firstRow.Cells(1, 1).Value ' 将前三列填成第一行的前三列
                cell.Offset(0, -2).Value = firstRow.Cells(1, 2).Value
                cell.Offset(0, -1).Value = firstRow.Cells(1, 3).Value
            End If
        End If
    Next cell
End Sub


```


# 分列

```
Selection.TextToColumns Destination:=Range("A1"), DataType:=xlDelimited, TextQualifier:=xlTextQualifierDoubleQuote, ConsecutiveDelimiter:=True, Tab:=True, Semicolon:=False, Comma:=False, Space:=True, Other:=False, FieldInfo:=Array(Array(1, 1), Array(2, 1), Array(3, 1), Array(4, 1), Array(5, 1), Array(6, 1), Array(7, 1)), TrailingMinusNumbers:=True
```

# 加引号

Sub 加引号()
    dim index_n as integer, row_n as integer, column as String
    ' 获取选定区域的行数
    row_n = Selection.Rows.Count
    index_n = 1
    column = ""

    ' 循环遍历每个单元格
    For Each cell In Selection
        If index_n < row_n Then
            ' 如果不是最后一行
            column = column & """" & cell.Value & """," & vbCrLf
        Else
            ' 如果是最后一行
            column = column & """" & cell.Value & """"
        End If
        index_n = index_n + 1
    Next cell
    debug.print column
End Sub


# 生成java 
```
Private Sub CommandButton1_Click()
    

    Dim columns() As String
    Dim sql As String, table_name As String
    Dim row_n As Long, index_n As Long, i As Range
    Dim field_name As String, field_comment As String, field As String

    ' 初始化 SQL 语句
    sql = "" & vbCrLf

    ' 获取选定区域的行数
    row_n = Selection.Rows.Count
    index_n = 1

    ' 遍历选定区域的每一行
    For Each i In Selection.Rows
        ' 获取每一行的数据
        Dim row As Variant
        row = Application.Transpose(Application.Transpose(i))

        ' 从数组中获取字段名、字段注释和表名
        field_name = row(1)
        field_type = row(2)
        field_comment = row(3)

        
        ' 构建字段字符串并添加到 SQL 语句中
        field = "/**" & vbCrLf & " * " & field_comment & vbCrLf & " */" & vbCrLf & "public " & field_type & " " & field_name & ";" & vbCrLf
        sql = sql & field

        index_n = index_n + 1
        Debug.Print index_n
    Next i

    ' 构建最终的 SQL 语句
    sql = sql & vbCrLf

    ' 输出 SQL 语句
    Debug.Print sql
    'TextBox1.Text = sql

End Sub



```


# 替换内容


```
Sub 替换内容()
      
    ' 循环遍历每个单元格
    For Each cell In Selection
        ' 检查单元格的值是否包含'
        If InStr(1, cell.Value, "'") > 0 Then
            ' 如果包含1，则替换为2
            cell.Value = Replace(cell.Value, "'", "")
        End If
        ' 检查单元格的值是否包含,
        If InStr(1, cell.Value, ",") > 0 Then
            ' 如果包含1，则替换为2
            cell.Value = Replace(cell.Value, ",", "")
        End If
        If InStr(1, cell.Value, "`") > 0 Then
            ' 如果包含1，则替换为2
            cell.Value = Replace(cell.Value, "`", "")
        End If
    Next cell
End Sub


```

# 生成sql 按钮
```
Sub concatSql()
    ' 拼接 SQL

    Dim columns() As String
    Dim sql As String, table_name As String, source_table_name As String
    Dim row_n As Long, index_n As Long, i As Range
    Dim field_name As String, field_comment As String, field As String, source_field_name As String
    

    ' 初始化 SQL 语句
    sql = "SELECT" & vbCrLf
    sql1 = sql

    ' 获取选定区域的行数
    row_n = Selection.Rows.Count
    index_n = 1

    ' 遍历选定区域的每一行
    For Each i In Selection.Rows
        ' 获取每一行的数据
        Dim row As Variant
        row = Application.Transpose(Application.Transpose(i))

        ' 从数组中获取字段名、字段注释和表名
        field_name = row(1)
        field_comment = row(2)
        table_name = row(4)
        source_table_name = row(5)
        source_field_name = row(6)
        
        ' 构建字段字符串并添加到 SQL 语句中
        If index_n < row_n Then
            ' 如果不是最后一行
            field = vbTab & field_name & ", -- " & field_comment & vbCrLf
            field1 = vbTab & source_field_name & vbTab & "as" & vbTab & field_name & ", -- " & field_comment & vbCrLf
        Else
            ' 如果是最后一行
            field = vbTab & field_name & " -- " & field_comment & vbCrLf
            field1 = vbTab & source_field_name & vbTab & "as" & vbTab & field_name & " -- " & field_comment & vbCrLf
        End If

        sql = sql & field
        sql1 = sql1 & field1

        index_n = index_n + 1

    Next i

    ' 构建最终的 SQL 语句
    sql = sql & vbCrLf & "FROM" & vbCrLf & table_name
    sql1 = sql1 & vbCrLf & "FROM" & vbCrLf & source_table_name

    ' 输出 SQL 语句
    Debug.Print sql1
    
    TextBox1.Text = sql
    TextBox2.Text = sql1
End Sub

Private Sub CommandButton1_Click()
    concatSql

End Sub

Private Sub Worksheet_SelectionChange(ByVal Target As Range)
On Error GoTo 0
   With Cells(Windows(1).ScrollRow, Windows(1).ScrollColumn)
   'updated by nirmal
      CommandButton1.Top = .Top + 20
      CommandButton1.Left = .Left + 1000
      TextBox1.Top = .Top + 20
      TextBox1.Left = .Left + 800
   End With
End Sub


```




# 生成sql

```
Sub concatSql()
    ' 拼接 SQL

    Dim columns() As String
    Dim sql As String, table_name As String
    Dim row_n As Long, index_n As Long, i As Range
    Dim field_name As String, field_comment As String, field As String

    ' 初始化 SQL 语句
    sql = "SELECT" & vbCrLf

    ' 获取选定区域的行数
    row_n = Selection.Rows.Count
    index_n = 1

    ' 遍历选定区域的每一行
    For Each i In Selection.Rows
        ' 获取每一行的数据
        Dim row As Variant
        row = Application.Transpose(Application.Transpose(i))

        ' 从数组中获取字段名、字段注释和表名
        field_name = row(1)
        field_comment = row(2)
        table_name = row(4)
        
        ' 构建字段字符串并添加到 SQL 语句中
        If index_n < row_n Then
            ' 如果不是最后一行
            field = vbTab & field_name & ", -- " & field_comment & vbCrLf
        Else
            ' 如果是最后一行
            field = vbTab & field_name & " -- " & field_comment & vbCrLf
        End If

        sql = sql & field

        index_n = index_n + 1
        Debug.Print index_n
    Next i

    ' 构建最终的 SQL 语句
    sql = sql & vbCrLf & "FROM" & vbCrLf & table_name

    ' 输出 SQL 语句
    Debug.Print sql
End Sub

```

# float button

```

Private Sub Worksheet_SelectionChange(ByVal Target As Range)
On Error GoTo 0
   With Cells(Windows(1).ScrollRow, Windows(1).ScrollColumn)
   'updated by nirmal
      CommandButton1.Top = .Top + 20
      CommandButton1.Left = .Left + 1000
   End With
End Sub

```


# 将内容输出到 文本框

* 文本框MultiLine 属性设置为true

```
Private Sub CommandButton1_Click()
 ' 拼接 SQL

    Dim columns() As String
    Dim sql As String, table_name As String
    Dim row_n As Long, index_n As Long, i As Range
    Dim field_name As String, field_comment As String, field As String

    ' 初始化 SQL 语句
    sql = "SELECT" & vbCrLf

    ' 获取选定区域的行数
    row_n = Selection.Rows.Count
    index_n = 1

    ' 遍历选定区域的每一行
    For Each i In Selection.Rows
        ' 获取每一行的数据
        Dim row As Variant
        row = Application.Transpose(Application.Transpose(i))

        ' 从数组中获取字段名、字段注释和表名
        field_name = row(1)
        field_comment = row(2)
        table_name = row(4)
        
        ' 构建字段字符串并添加到 SQL 语句中
        If index_n < row_n Then
            ' 如果不是最后一行
            field = vbTab & field_name & ", -- " & field_comment & vbCrLf
        Else
            ' 如果是最后一行
            field = vbTab & field_name & " -- " & field_comment & vbCrLf
        End If

        sql = sql & field

        index_n = index_n + 1
        Debug.Print index_n
    Next i

    ' 构建最终的 SQL 语句
    sql = sql & vbCrLf & "FROM" & vbCrLf & table_name

    ' 输出 SQL 语句
    Debug.Print sql
    Me.Enabled = False
    Me.BorderStyle = fmBorderStyleNone
    TextBox1.Text = sql
End Sub

```