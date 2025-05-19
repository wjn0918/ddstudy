---
title: notebook
---
# jupyter notebook
1. %matplotlib inline 这个命令告诉Jupyter Notebook或IPython环境将matplotlib生成的图表直接嵌入到笔记本的单元格中，而不是在单独的窗口中弹出图表。这对于交互式数据分析和可视化非常方便，因为你可以在同一个界面中编写代码、运行程序并立即看到图形结果，无需额外操作。
2. %config InlineBackend.figure_format = 'png' 这行代码进一步配置了matplotlib的Inline Backend（内联后端），指定了图表保存和显示的格式为PNG。PNG是一种无损压缩的位图图像格式，支持透明度，适合网页展示和大多数打印需求。通过设置这个配置，当你在Jupyter Notebook中生成图表时，即便放大也不会失真，保证了较好的视觉质量。其他可选的格式还有'svg'（可缩放矢量图形，适合需要高分辨率或需要频繁放大的场景）和'retina'（针对高分辨率屏幕优化的图像格式）等。


# 环境离线迁移
conda pack -n notebook -o notebook.tar.gz

* jupyter kernels  更改
/envs/notebook/share/jupyter/kernels/python3



conda env export --name foo_env > foo.yaml
conda env update --name bar_env --file foo.yaml