---
title: 转载 | Altium规则详解及设置
date: 2016-09-10 10:47:34
categories:
  - HW
tags:
  - Altium
  - PCB Design
---

在Altium中进行PCB的设计时，经常会使用规则（Rule）来进行限定以确定线宽孔径等参数，此文将简要的介绍规则中的一些标量代表了什么。

<!--more-->

**Electrical**------电气规则。安全间距，线网连接等

**Routing**------布线，线宽、过孔形状尺寸、布线拓扑、布线层、封装出线等

**SMT**------Surface Mount Technology，表面组装技术（表面贴装技术），贴片。贴片元件焊盘的一些要求

**Mask**------掩膜，阻焊和焊膏的扩展

**Plane**------内电层和铺铜。与焊盘的连接方式

**Testpoint**------测试点

**Manufacturing**------加工。孔、焊盘、丝印和阻焊的尺寸及相关关系

**HighSpeed**------高速信号。串扰、线长、配长、过孔数量等高速信号相关的

**Placement**------放置。元件放置与元件间距等

**SignalIntegrity**------信号完整性。走线阻抗及高速信号的过冲、摆率等

**同一规则下可以包含（新建）多个规则，并为每个规则设置不同的使用范围和优先级，以根据具体需求实现灵活多样的规则。**

*设置优先权的方法：对话框右下角Priorities，进入设置。导入规则.rul文件*



## 规则详细描述

**Clearance** 安全距离，包括元件焊盘与焊盘、焊盘与导线、导线与导线之间的最小距离

**Short Circuit** 短路，及是否允许导线交叉短路，默认不允许

**Un-connect Net** 未布线网络，可以指定网络、检查网络布线是否成功，如果不成功，将保持用飞线连接

**Un-connected Pin** 未连接管教，对指定的网络检查是否所有元件管脚都连线了

**Width** 导线宽度

**Routing Toplogy** 布线拓扑。拓扑规则定义是采用布线的拓扑逻辑约束，常用的布线约束为统计最短逻辑规则，用户可以根据具体设计选择不同的布线拓扑规则：

**Shortest** 最短规则设置，所有节点的连线最短规则

**Horizontal** 水平规则设置，连接节点的水平连线最短规则

**Vertical** 垂直规则设置，连接节点的垂直连线最短规则

**Daisy Simple** 简单雏菊规则设置，采用链式连通法则，从一点到另一点连通所有节点，并使连线最短

**Daisy-MidDriven** 雏菊中点规则设置，选择一个Source源点，以它为中心向左右连通所有节点，并使连线最短

**Daisy Balanced** 雏菊平衡规则设置，选择一个Source源点，将所有中间节点数目平均分成组，所有组都连接在源点上，并使连线最短

**Star Burst**（星形）规则设置选择一个源点，以星形方式去连接别的节点，并使连线最短。

**Routing Priority** 布线优先级别

**Routing Layers** 布线层设置

**Not Used** 该层不进行布线； 

**Horizontal** 该层按水平方向布线 ;

**Vertical** 该层为垂直方向布线； 

**Any** 该层可以任意方向布线；

+ 10n Clock 该层为按一点钟方向布线； 
+ 20n Clock 该层为按两点钟方向布线； 
+ 40n Clock 该层为按四点钟方向布线； 
+ 50n Clock 该层为按五点钟方向布线； 
+ 45Up 该层为向上 45 °方向布线、 
+ 45Down 该层为向下 45 °方法布线； 
+ Fan Out 该层以扇形方式布线。
+ 对于系统默认的双面板情况，一面布线采用 Horizontal 方式，另一面采用 Vertical 方式。 
+ Routing Corners 拐角。45、90、圆角
+ Routing Via Style 导孔。

 

## 组焊层设计规则

**Solder Mask Expansion** 组焊层延伸量。用于设计从组焊层之间的距离，在电路板制作时，组焊层要预留一部分空间给焊盘，这个延伸量就是防止组焊层和焊盘相重叠。

**Paste Mask Expansion** 表面粘着元件延伸量。表面粘着元件的焊盘和焊锡层孔之间的距离。



## 内层设计规则

**Plane** 用于多层板

**Power Plane Connect Style** 电源层连接方式。用于设置导孔到电源层的连接

**Conner Style** 下拉列表。设置电源层和导孔的连接风格

**Relief Connect** 发散状连接

**Direct Connect** 直接连接

**No Connect** 不连接

**Conductor Width** 设置导通的导线宽度

**Conuctors** 选择连通的导线的数目

**Air-Gap** 设置空隙的间隔宽度

**Expansion** 设置从导孔到空隙的间隔之间的距离

**Power Plane Clearance** 电源层安全距离。设置电源层和穿过它的导孔之间的安全距离，即放置导线断路的最小距离

**Polygon Connect Style** 敷铜连接方式。多边形敷铜与焊盘之间的连接方式

**Connect Style, Conductors, Conductor width** 敷铜与焊盘之间的连接角度：90、45

 

## 测试点设计规则

用于设计测试点的形状、用法

**Testpoint Style** 测试点风格。

**Size** 测试点的大小

**Grid Size** 格点的大小

**Allow testpoint under component** 选择是否允许将测试点放置在元件下面

**TestPoint Usage** 测试点用法

**Allow multiple testpoints on same net** 设置是否可以在同一网络上允许多个测试点存在

**Testpoint** 选项区域中的单选项选择对测试点的处理，可以使Required（必须处理）、Invalid（无效的测试点）、Don’t care（可忽略的测试点）




## 电路板制造设计规则

**Minimum annular Ring** 最小焊盘环宽

**Acute Angle** 导线夹角设置

**Hole size** 导孔直径设置

**Measurement Method** Absolute 以绝对尺寸来设计；Percent以相对的比例来设计

**Layers Pais** 使用半层对 在设计多层板时，如果使用了盲导孔，就要在这里对板层对进行设置

**本文摘抄转载自[Altium Designer规则设置](http://www.cnblogs.com/perfy/p/3957601.html)，在此表示感谢**