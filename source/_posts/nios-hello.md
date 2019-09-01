---
title: 原创 | 迈出 NIOS 的第一步 HelloNIOS
date: 2016-12-13 15:47:34
categories:
  - FPGA
tags:
  - NIOS
---

Altera 官方推出 NIOS 已经很久了，个人感觉 C+V 代码配合会是后面 FPGA 使用的一个主流，由 C 来完成一些对时序要求不高，对功能要求偏高的部分，比如运动控制等；由 V 来配合时序完成高时序要求的需求以及一些底层的驱动供 C 来调用，这样的设计结构感觉更加合理有效，也更加适合于一些大型工程。但是有一点不好的就是程序可移植性可能有点差，毕竟使用 Eclipse 编辑环境（我也不确定，反正个人感觉移植起来有些麻烦）。

好了，本文就开始我们的第一个例程，**HelloNIOS**。软件语言中经典的 HelloWorld 在这里变成了 HelloNIOS，看起来也很不错。

<!--more-->

##  简介

其实，网络上有关于 NIOS 的教程已经很多了，本文在此只作为我自己的一个学习使用记录。首先，要用 NIOS，你肯定得有相匹配的硬件吧，在这里先来介绍下我自己的硬件环境。

* 硬件：开发板黑金 AX301
* 软件：QuartusII 13.0sp1，NIOS13.0sp1

最关键的因素就是这些了，开发板很普通，买了后觉得资源有些少了，不过一些简单的开发以及使用 NIOS 那还是足够了，物尽其用，搞起来。

先说下所参考的一些资料，《NIOS 的奇幻漂流》和《NIOS 那些事儿》，感觉都是很经典的资料，完全可以用作入门。

## Quartus工程建立

这里和普通的硬件 Quartus 工程建立没有什么区别，在这里就不多说，简要提过。

1. 建立 Quartus 工程，分配好各部分所在文件夹（这是个人习惯，现在我一般的框架如下图）
	![文件框架](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20160626-folder-struct.png)
	其中 `ipcore` 用来存放自创建的官方IP核，`tcl` 用于存放tcl引脚文件，`verilog` 用于存放个人编写的V代码。

2. 创建对应的 PLL，这里是否创建 PLL 自行决定，因为我们要用到板上资源 SDRAM，其需要 100MHz 的时钟，而我们的输入是 50MHz，所以此处需要一个 PLL。

3. 建立完PLL后，我们建立 Qsys。Qsys 就是之前版本中的 SOPC Builder，其主要就是创建一个虚拟 SOPC 出来。Tools -->> Qsys 可以打开，打开后我们可以看到如下界面。
	![Qsys初始界面](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20160626-qsys-initial.png)

4. 依次添加NIOS、SYSID、SDRAM、EPCS、JTAG、添加后进行改名连线。改名方法为选中 NAME 后按 “2” 或者 “R” 即可，我一般会将这几部分的名字全部改为大写。其中可能会有部分 Warning 或者 Error 出现，下面对一些需要注意的点进行了说明。
	* 下图为添加所有部件后的示意图
	![Qsys 添加后示意图](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20160626-qsys-all.png)
	* 按照一定的规则连线后，可以参考下图形式连线，下方仍然发现了部分如下Error的存在。
	![Qsys 参考连线图](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20160626-qsys-linked-all.png)
	![Qsys-Error](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20160626-qsys-error.png)
	* 这里就需要对NIOS核进行一定的设置，双击打来NIOS核，进行如下的设置。设置完成后就可以看到Error消失了。
	![NIOS 核配置](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20160626-qsys-nios.png)
	* 当然这时下方还会出现一些有关于地址线错误的Warning或者Error，这是由于很多部件的地址占用空间相同了，这在右侧可以看出，类似于如下截图。
	![](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20160626-qsys-error-address.png)
	* 这时可以点击System->Assign Base Address进行地址线的自动分配，这里我有一个习惯就是会把EPCS模块的地址线固定为0x0，从上面连线图也可以看出。
	* 以上完成后要注意我们最后一列的中断IRQ，也要记得将他们连起来。
	* 之后点击上边标签栏中的Generation进行生成，该页面记得将以下部分勾选。
	![Qsys-Generation 勾选](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20160626-qsys-generation-all.png)
	* 至此，Qsys中的配置部分结束。

5. 在 Quartus 顶层中添加 PLL 和 Qsys，参考资料上多用原理图的形式进行连接，我一般是使用代码的方式进行连接，这部分就看个人喜好了。使用代码连接可移植性好些但是没有原理图形式直观。

6. 然后编译，将 SOF 下载到 FPGA 开发板中。至此，Quartus 中的所有工作完毕。

## NIOS工程建立

这部分按照参考资料说明书来即可，十分简单，简写如下。

1. 选择一个空间用于存放工程，我一般放于 Qsys 的目录下
2. File -->> New -->> NIOS II Application and BSP Template
3. 选中 Quartus 下的 sopcinfo 文件，然后命名工程，一路 Next 就行
4. 工程生成后，选中左边的文件夹，右键 NIOS II -->> Generate BSP
5. 生成后，Ctrl + B 进行编译
6. 编译完成后，打开 Run-Configuation，进行下载配置，Apply，Run
7. 最后就可以等待调试框中的结果了
8. 最后放上成功的结果
	![HelloNios](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20160626-nios-hellonios.png)















































