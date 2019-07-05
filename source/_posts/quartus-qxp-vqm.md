---
title: 转载 | Quartus代码保护之网表文件
date: 2016-12-7 15:47:34
categories:
  - Quartus
tags:
  - Quartus
---

当项目过程中，不想给甲方源码时，该如何？我们可以用网表文件qxp或者vqm对资源进行保护。
本文主要讲解这两个文件的具体生成步骤。

<!--more-->


## 基本概念

QuartusII的qxp文件为QuartusII Exported Partition，用于创建综合或者PAR之后的网表文件。
QuartusII的vqm文件为verilog quartusII mapping，只能保存综合后，PAR前的综合结果。

## qxp文件生成

1. 在quartusII的Project Navigator中选中欲创建qxp的module文件，右击，选择“Design Partition > Set as Design Partition”。
2. 综合整个工程，想出PAR后的qxp就需要编译整个工程。
3. 点击菜单“Process”，选择“Start > Start Partition Merge”，以创建完整的module网表。
4. 点击菜单“Project”，选择“Export Design Partition”。
5. 在弹出窗口中选择想要的层次和网表选项，即可导出qxp文件。
注：使用时，仍需右击选择“Set as Design Partition”，否则，有时候会出错，只是有时候而已哦。通过RTL查看器看到的qxp模块是空的，但PAR后即可看到里面的东东了。

## vqm文件生成

1. 创建以相应module为顶层的工程。
2. 点击菜单“Process”，选择“Start > Start VQM Writer”，即可得到vqm文件。
　　注：有的器件不支持vqm哦，此时只能用qxp了。

## 参考

1. [（原创）详解Quartus导出网表文件：.qxp和.vqm](http://www.cnblogs.com/adamite/p/qxp_vqm.html)