---
title: 转载 | Matlab 之静态文本多行输出
date: 2016-11-10 10:47:34
categories:
  - Matlab
tags:
  - Matlab
---

转载文章，原文链接：[Matlab 中的静态文本框中显示多行内容](http://blog.sina.com.cn/s/blog_4d633dc70100nwzf.html)

有时候，我们在 GUI 中利用静态文本框显示程序的结果，但是结果很长，一行未必可以显示的开，而静态文本框不像 edit 或 listbox 那样通过滚动条来显示多行内容，即便设置了 max 和 min 属性也是一样的。

于是，怎么在静态文本框中显示多行是很有意义的。

<!--more-->

## 解决方法 ##

利用函数 **textwrap**
```matlab
figure('units', 'normalized', 'position', [0.4 0.4 0.4 0.3]);
h = uicontrol('Style','Text','fontsize',16);
string = {'静态文本框为什么是静态的？','因为不能像编辑框一样滚动显示其中的内容',...
    '如果想在静态文本框中多行显示','按照这种方式就可以实现','调用textwrap函数啊！'};
[outstring, newpos] = textwrap(h, string);
set(h,'String', outstring, 'Position', newpos);
```
## 显示结果 ##

在这里需要**注意**的是，一行中间最好不要有空格，如果有的话，函数会把它分配成两个段落的。
![Matlab 中的静态文本框中显示多行内容](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20160610-matlab-gui-multi-row-text.png)
