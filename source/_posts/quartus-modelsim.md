---
title: 原创 | Quartus 中调用 Modelsim 波形仿真
date: 2016-11-10 15:50:34
categories:
  - Quartus
tags:
  - Quartus
  - Modelsim
---
在使用 QuartusII 软件的过程中，经常地需要跑仿真，那么说到仿真就不得不说 Modelsim 这个仿真软件了，我们这里介绍下该软件在 QuartusII 中的使用方法。　

<!--more-->

## 建立Quartus和Modelsim的连接

如果是首次使用，需建立连接。Tools -->> Options -->> EDA Tools Option，在 Modelsim-Altera 处选择应用软件路径。比如 “D:\altera\13.0\modelsim_ae\win32aloem” 这种。

## 建立测试文件

Processing -->> Start -->> Start Test Bench Template Writer，建立好之后自行进行编写测试文件。13.0 版本的 vt 测试文件在 ../simulation/modelsim/ 路径下。

## 添加测试文件

Assignments -->> Setting-->> EDA Tool Setting。

![图1](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20160601-quartus-modelsim-Fig1.png)

在下方 NativeLink Setting 处选择刚才的测试文件。完整填写下图后添加测试工程。

![图2](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20160601-quartus-modelsim-Fig2.png)

## 编译执行仿真

上述操作完成进行编译，编译完成后 Tools -->> Run Simulation Tool -->> RTL Simulation 即可进行仿真操作，之后 Modelsim 就会打开并按照测试文件进行执行。