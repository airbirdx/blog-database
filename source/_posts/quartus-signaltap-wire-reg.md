---
title: 原创 | 如何使用SignalTap观察wire与reg值
date: 2016-11-10 11:47:34
categories:
  - Quartus
tags:
  - SignalTap
---

在FPGA程序调试时，我们除了仿真还经常的会用到SignalTap进行板级调试，其可以真实有效的反应某些变量的变化，方便我们理解内在跳转，方便Debug的运行。SignalTap需要制定时钟，根据需求进行选择，其采样遵循奈奎斯特因采样定律。

我们在Debug中有时会经常遇到这样的情况，在SignalTap中并不能观察到所有的变量值。有些变量添加进入面板后会变红，这就表示SignalTap抓取不到此数值。出现这一现象的原因是，综合器在综合时对一些变量进行了优化，所以就显示不出来了。下文将针对两种变量类型，wire和reg来分别讲述如何让其正常的显示出来。这一部分的知识其实很简单就是，基本思想就是使用综合属性Synthesis Attribute来控制综合时的一些优化。

<!--more-->


## wire型变量

有关于变量的综合属性这一块也可以在Quartus中的language template中查看。wire型变量的综合属性在Quartus 13中的template中显示如下，其主要命令为keep命令。Quartus软件中给出了相关的介绍。
```verilog
// Prevents Quartus II from minimizing or removing a particular
// signal net during combinational logic optimization.    Apply
// the attribute to a net or variable declaration.
	
(* keep *) wire <net_name>;
(* keep *) reg <variable_name>;
```
其主要是为了防止相关wire型变量在综合时被优化或者是被省略。

总结出wire型变量的综合属性配置方法有以下两种。

```verilog
1. (* keep * )    wire    <net_name>;
2. wire    <net_name>/* synthesis keep */;
```

其中，第一种写法为verilog-2001标准，第二种为之前的标准，两者可兼容。需要注意的是在采用第二种写法时，注释部分一定要写在分号之前。

## reg型变量

reg 型变量的综合属性在Quartus 13中的template中显示如下，其主要命令为preserve和noprune命令。

```verilog
// Prevents Quartus II from optimizing away a register.     Apply
// the attribute to the variable declaration for an object that infers
// a register.

(* preserve *) <variable_declaration>;
(* preserve *) module <module_name>(...);
```

防止优化掉某一个reg型的部分或整体，可以用于某一个特定的变量也可以用于一个module中的所有reg型变量。

```verilog
// Prevents Quartus II from removing or optimizing a fanout free register.
// Apply the attribute to the variable declaration for an object that infers
// a register.

(* noprune *)  <variable_declaration>;
```

防止优化掉一个没有扇出的reg型变量，有可能是无关量，有可能是中间量。

总结出reg型变量综合属性配置的方法有以下几种。

	1. (* noprune *)    reg    <variable>;
	2. (* preserve *)    reg    <variable>;
	3. (* preserve *)    module    <module_name>(...);
	4. reg    <variable>/* synthesis noprune */;
	5. reg    <variable>/* synthesis preserve */;
	6. module    <module_name>(...)/* synthesis preserve */;

同样有两种写法，是两种标准，读者可任意选择一款觉得方便的。同样注意的是分号的位置，因为比较重要多一多说几遍。reg型有两种，一般自行选择，如果不行就换另外一种试试，总是会有一款ok的形式。

## 总结

有了这样的可调综合属性，在进行板级调试时可以任意添加中间变量来观察运行状况，极大程度上方便了Debug，提高了效率。