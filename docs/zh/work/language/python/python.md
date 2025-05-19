---
title: Python
---

:::warning

禁止使用service作为包名

:::


## pip

```
-i https://pypi.tuna.tsinghua.edu.cn/simple/
```

## py-roughviz

手绘风

```
pip install py-roughviz
```






## 显式指定数据类型

x: int = 5

## 数组笛卡尔积

```

import numpy as np
from itertools import product

# 定义原始数组
a = np.arange(1, 31)
b = np.arange(1, 9)
c = np.arange(1, 17)

# 创建笛卡尔积
cartesian_product = list(product(a, b, c))

# 将笛卡尔积转换为numpy数组，并重塑为所需形状
result = np.array(cartesian_product).reshape(-1, 3)

# 输出结果
print(result)

```



## 打包exe


pyinstaller.exe -w --icon= -F .\app.py


https://cdkm.com/cn/svg-to-ico#google_vignette




## IPython 

```
from IPython.display import display, Math

# LaTeX表达式
cost_function_latex = r'J(\theta) = \frac{1}{2m} \sum_{i=1}^{m} \left(h_{\theta}\left(x^{(i)}\right) - y^{(i)}\right)^2'
feature_function_latex = r'h_{\theta}(x) = \theta^T X = \theta_0 x_0 + \theta_1 x_1 + \theta_2 x_2 + \dots + \theta_n x_n'

# 显示LaTeX公式
display(Math(cost_function_latex))
display(Math(feature_function_latex))

```


## rich 

Rich is a Python library for rich text and beautiful formatting in the terminal.

```
from rich import print
print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:")

```



## notebook 

python 3.10.13
notebook==6.4.12
jupyter_contrib_nbextensions
pip install jupyter_nbextensions_configurator widgetsnbextension 

pip install https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tarball/master

jupyter contrib nbextension install --user

jupyter nbextensions_configurator enable --user
jupyter nbextension install --py widgetsnbextension --user
jupyter nbextension enable --py widgetsnbextension --user

pip install traitlets==5.9.0
pip install Cython
pip install pyzmq==19.0.2



jupyter nbextensions_configurator disable --user



## 交互式控件 

pip install ipywidgets 



## kernel error 

jupyter kernelspec list  查看安装位置

进入目录，查看 kernel.json文件






## 自动生成requirements.txt

```
pip install pipreqs
pipreqs --debug  --encoding utf8 --pypi-server https://pypi.tuna.tsinghua.edu.cn/pypi/ --force ML-face-recognition/ 
pip install -r requirements.txt
```

* 获取对象属性

def getattr(object, name, default=None): # known special case of getattr
    """
    getattr(object, name[, default]) -> value
    
    Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.
    When a default argument is given, it is returned when the attribute doesn't
    exist; without it, an exception is raised in that case.
    """

## 排序
```
# 按照 "text" 键倒序排列
sorted_data = sorted(data, key=lambda x: x["text"], reverse=True)

print(json.dumps(sorted_data,ensure_ascii =False))

```



## 执行子程序


```
def exce_script(target_table_name):
    """
    执行脚本
    :return:
    """

    import subprocess

    # 指定项目B的根路径
    project_b_path = r"D:\wjn\gitee\jzDataMigrate"

    # 设置环境变量 PYTHONPATH
    env = os.environ.copy()
    env["PYTHONPATH"] = project_b_path


    # 指定虚拟环境的Python可执行文件路径和要运行的脚本路径
    venv_python_exe = r"D:\wjn\gitee\jzDataMigrate\.venv\Scripts\python.exe"
    script_path = f"D:\wjn\gitee\jzDataMigrate\etl\jz\\{target_table_name}.py"

    # 使用subprocess模块调用虚拟环境中的Python脚本
    try:
        subprocess.run([venv_python_exe, script_path], check=True, env=env)
    except subprocess.CalledProcessError as e:
        print(f"Error executing the script: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```