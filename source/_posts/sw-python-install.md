---
title: 原创 | Python及其使用库安装
date: 2018-5-3 17:16:00
categories:
  - Python
tags:
  - Python
---

本文主要讲述Python及其使用库的安装，例如Pillow图形处理的库等。

<!--more-->

## 下载Python

进入[Python](https://www.python.org/)的官网后选择合适的版本进行下载，很简单的步骤，不多说。在这里我们选择Python3版本进行安装。

## Python安装

使用下载好的文件进行安装，傻瓜式操作，一路按照默认点击[Next]就行。

需要**注意**的一点是在安装过程中记得将Python添加到PATH中，不然后续需要手动编辑电脑的环境变量进行添加，既然提供了省事的方案，何必再麻烦一遍呢，当然不嫌折腾的也可以自己手动操作。

## Pillow库安装

可以使用python自带的`easy_install`或者`pip`工具进行安装。

在Python安装完成后使用`Everything`搜索`pip.exe`，然后选择打开其文件路径，可以看到几种的工具。

![Everything搜索](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20180503-sw-python-everything-search-pip.png)

![安装工具/脚本](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20180503-sw-python-install-script.png)

右键打开`PowerShell`工具，在其中键入

```
.\pip.exe install Pillow
```

之后回车等待即可，当进度条100%后，第三方Pillow库安装完成。

![使用PIP安装Pillow](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20180503-sw-python-pip-pillow.png)