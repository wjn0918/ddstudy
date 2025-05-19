# 分页

```
import pandas as pd
import ipywidgets as widgets
from IPython.display import display

# 创建一个示例的Pandas DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily', 'Frank', 'Grace', 'Hannah', 'Ian', 'Julia'],
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']
}
df = pd.DataFrame(data)

# 设置每页显示的行数
rows_per_page = 5

# 计算总页数
total_pages = len(df) // rows_per_page + (1 if len(df) % rows_per_page > 0 else 0)

# 创建一个DataFrame小部件
df_widget = widgets.Output()

# 定义一个函数，用于在DataFrame小部件中显示指定页的数据
def display_page(page_number):
    start_idx = (page_number - 1) * rows_per_page
    end_idx = start_idx + rows_per_page
    with df_widget:
        df_widget.clear_output(wait=True)
        display(df.iloc[start_idx:end_idx])

# 创建一个分页控件
page_slider = widgets.IntSlider(value=1, min=1, max=total_pages, description='Page:', continuous_update=False)

# 当滑块值变化时显示对应页的数据
def on_page_change(change):
    display_page(change.new)
    
page_slider.observe(on_page_change, 'value')

# 初始化时显示第一页的数据
display_page(1)

# 显示分页控件和DataFrame小部件
display(page_slider)
display(df_widget)

```


# 下载

```
import pandas as pd
import ipywidgets as widgets
from IPython.display import display, FileLink

# 创建一个示例的Pandas DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily', 'Frank', 'Grace', 'Hannah', 'Ian', 'Julia'],
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']
}
df = pd.DataFrame(data)

# 创建一个按钮小部件
button = widgets.Button(description="下载Excel")

# 定义一个函数，用于在点击按钮时保存DataFrame为Excel文件，并创建一个下载链接
def save_and_download(_):
    df.to_excel('data.xlsx', index=False)
    download_link = FileLink('data.xlsx', result_html_prefix="点击下载: ")
    display(download_link)

# 将按钮的点击事件与保存函数关联
button.on_click(save_and_download)

# 显示按钮
display(button)

```


```


import ipywidgets as widgets
from IPython.display import display

# 创建一个样式字典，用于指定描述的宽度
style = {'description_width': 'initial'}

# 创建一个文本框小部件，用于接收用户输入的预算金额
budget_input = widgets.FloatText(
    value=1000.0,
    description='预算金额（元）:',
    disabled=False,
    style=style,
    layout=widgets.Layout(width='300px')  # 设置宽度
)

# 创建分割线
separator = widgets.HTML(value="<hr>", layout=widgets.Layout(margin='10px 0'))


# 创建多个复选框，用于让用户选择需要采购的资产类型
asset_types = [
    '其他设备器具', '空调', '生活设备（电视、热水器、开水机等）', '家具', '生产设备',
    '房屋构筑物', '业务用车', '物流配送用车', '台式电脑', '笔记本电脑',
    '其他电子设备', '服务器、网络设备', '打印、复印设备', '显示屏、音响等会议设备',
    '摄影、摄像设备', '低值易耗品', '土地', '计算机软件'
]

asset_type_checkboxes = [
    widgets.Checkbox(value=False, description=asset_type, style=style) 
    for asset_type in asset_types
]

# 使用VBox和HBox容器进行布局
input_box = widgets.VBox([budget_input], layout=widgets.Layout(margin='0 0 20px 0'))
checkboxes_box = widgets.HBox(asset_type_checkboxes, layout=widgets.Layout(flex_flow='row wrap'))

# 显示预算金额输入框、分割线和资产类型多选框
display(input_box)
display(separator)
display(checkboxes_box)

# 定义一个函数，用于更新变量a和b的值
def update_values(change):
    global a, b
    a = budget_input.value
    b = [checkbox.description for checkbox in asset_type_checkboxes if checkbox.value]
    print("预算金额:", a)
    print("选择的资产类型:", b)

# 将函数与预算金额输入框和资产类型多选框的observe方法关联
budget_input.observe(update_values, names='value')
for checkbox in asset_type_checkboxes:
    checkbox.observe(update_values, names='value')

# 初始化时获取一次初始值
update_values(None)


```


```
import ipywidgets as widgets
from IPython.display import display

df_result = pd.DataFrame()


# 定义一个函数，用于在DataFrame小部件中显示指定页的数据
def display_page(page_number):
    global df_result
    start_idx = (page_number - 1) * rows_per_page
    end_idx = start_idx + rows_per_page
    with df_widget:
        df_widget.clear_output(wait=True)
        if len(b) == 0:
            df_filtered = df
        else:
            df_filtered = df[df['big_type'].isin(b)]
        df_sorted = df_filtered.sort_values(by='asset_score', ascending=True)
        df_result = df_sorted
        display(df_sorted.iloc[start_idx:end_idx])
         



# 创建一个样式字典，用于指定描述的宽度
style = {'description_width': 'initial'}

# 创建一个文本框小部件，用于接收用户输入的预算金额
budget_input = widgets.FloatText(
    value=1000.0,
    description='预算金额（元）:',
    disabled=False,
    style=style,
    layout=widgets.Layout(width='300px')  # 设置宽度
)

# 创建分割线
separator = widgets.Output(layout={'border': '1px solid black'})


# 创建多个复选框，用于让用户选择需要采购的资产类型
asset_types = [
    '其他设备器具', '空调', '生活设备（电视、热水器、开水机等）', '家具', '生产设备',
    '房屋构筑物', '业务用车', '物流配送用车', '台式电脑', '笔记本电脑',
    '其他电子设备', '服务器、网络设备', '打印、复印设备', '显示屏、音响等会议设备',
    '摄影、摄像设备', '低值易耗品', '土地', '计算机软件'
]

# 创建一个按钮
update_button = widgets.Button(description="更新")
download_button = widgets.Button(description="下载结果")
download_link_out = widgets.Output()

asset_type_checkboxes = [
    widgets.Checkbox(value=False, description=asset_type, style=style) 
    for asset_type in asset_types
]

# 使用VBox和HBox容器进行布局
# 将按钮和预算金额放在同一行
input_row = widgets.HBox([budget_input, update_button, download_button, download_link_out])
checkboxes_box = widgets.HBox(asset_type_checkboxes, layout=widgets.Layout(flex_flow='row wrap'))

# 显示预算金额输入框、按钮、分割线和资产类型多选框
display(input_row)
display(separator)
display(checkboxes_box)

# 定义一个函数，用于更新变量a和b的值
def update_values(change):
    global a, b
    a = budget_input.value
    b = [checkbox.description for checkbox in asset_type_checkboxes if checkbox.value]
    download_link_out.clear_output()
    display_page(1)
    
    # 计算总页数
    if len(b) == 0:
        total_pages = len(df) // rows_per_page + (1 if len(df) % rows_per_page > 0 else 0)
    else:
        total_pages = len(df[df['big_type'].isin(b)]) // rows_per_page + (1 if len(df[df['big_type'].isin(b)]) % rows_per_page > 0 else 0)
    
    # 更新分页控件的最大值
    page_slider.max = total_pages


# 定义一个函数，用于在点击按钮时保存DataFrame为Excel文件，并创建一个下载链接
def save_and_download(_):
    df_result.to_excel('data.xlsx', index=False)
    download_link = FileLink('data.xlsx', result_html_prefix="点击下载: ")
    download_link_out.clear_output()
    with download_link_out:
        display(download_link)
    
    
    
# 将更新按钮的on_click方法与更新值的函数关联
update_button.on_click(update_values)
download_button.on_click(save_and_download)

# 初始化时获取一次初始值
update_values(None)



#############################################

big_type = []
asset_name = []
use_y = []

for i in asset_type:
    for j in range(10):
        big_type.append(i)
        asset_name.append(i + "_" + str(j))
        use_y.append(j)
        
data = pd.DataFrame({"asset_name": asset_name, "big_type": big_type, "use_y": use_y})
data['use_y_limit'] = 3
data['best_use_y'] = 5
df = model_score_asset(data)



# 设置每页显示的行数
rows_per_page = 5

# 计算总页数
total_pages = len(df) // rows_per_page + (1 if len(df) % rows_per_page > 0 else 0)

# 创建一个DataFrame小部件
df_widget = widgets.Output()



# 创建一个分页控件
page_slider = widgets.IntSlider(value=1, min=1, max=total_pages, description='Page:', continuous_update=False)

# 当滑块值变化时显示对应页的数据
def on_page_change(change):
    display_page(change.new)
    
page_slider.observe(on_page_change, 'value')

# 初始化时显示第一页的数据
display_page(1)

# 显示分页控件和DataFrame小部件
display(separator)
display(page_slider)
display(df_widget)


```