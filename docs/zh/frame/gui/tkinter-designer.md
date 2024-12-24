---
title: Tkinter-Designer
---

基于figma自动生成tkinter gui

## 安装

```
conda create -n gui python==3.10
conda activate gui

git clone https://github.com/ParthJadhav/Tkinter-Designer.git

cd Tkinter-Designer

pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple/ -r requirements.txt


python gui/gui.py


* check_hostname requires server_hostname


或者使用下面的命令降低版本：
pip install urllib3==1.25.8

```


## 使用

首先，创建一个框架作为您的 Tkinter 窗口。


### 支持的命名

| figma元素名称 | Tkinter元素 |
| ------------- | ----------- |
| Button        | Button      |
| Line          | Line        |
| Rectangle     | Rectangle   |
| TextArea      | Text Area   |
| TextBox       | Entry       |
| Image         | Canvas.Image() |


### 添加图片

```
可以使用形状和/或图像创建图像
如果您使用多个形状/图像，您必须通过选择它们并按 CTRL/⌘ 将它们组合在一起。 + G
在此之后将元素或组命名为“Image”。
```


### 添加文本

```
文本（普通文本）

使用 T 键激活文本工具，然后根据需要添加文本
在 Tkinter Designer 中使用时不必重命名文本
明确按下 Return 或 Enter 键移动到下一行。
```

### 输入（单行用户输入）

```
使用 R 激活矩形工具
根据您的喜好调整矩形
确保矩形命名为“TextBox”
```









### 文本区域（多行用户输入）
```
使用 R 激活矩形工具
根据您的喜好调整矩形
确保矩形命名为“TextArea”
```

## 矩形
```
使用 R 激活矩形工具
根据您的喜好调整矩形
确保矩形被命名为“Rectangle”
```
## 按钮
```
添加一个元素作为 GUI 中的按钮
可选：为按钮添加文本
在按钮下方的图层上创建一个矩形
更改矩形的颜色以匹配背景
选择按钮、矩形和任何可选文本，然后将它们与CTRL/⌘ + G
将组命名为“Button”

```