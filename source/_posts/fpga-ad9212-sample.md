---
title: 原创 | AD9212采样方法
date: 2016-11-10 10:42:28
categories:
  - FPGA
tags:
  - FPGA
---

## 随记
最近由于工程原因用到ADC的采样，选用了ADI公司的AD9212芯片，八通道10位ADC。在进行ADC的采样时，看到的想到的几种方法，在这里做个笔记记录一下。

## AD9212简介
详细说明可以在[ADI官网](http://www.analog.com/cn/index.html)上进行搜索查看，具体的一些性能细节这里就不进行详细的介绍了。
ADC芯片在某一时刻采集到电压数据后会在一个时钟周期内将数据串行的输出，若使用FPGA对数据进行接收，所需要做的操作就只是一个串并转换，还是比较简单的对吧。在这里由于AD9212的数据传输是使用的LVDS输出，也可以使用Altera官方（对，我们用的是A家的芯片）的LVDS_RX的IP核进行接收。下面我们把AD9212的一个时序图放上来作为镇文之图。
![镇文之时序图](http://o85gvbiad.bkt.clouddn.com/20161024-ad9212-original-timing.png)
从图中可以看出DCO作为数据传出的时钟是上下边沿触发的，在每个边沿数据D有效。FCO作为帧定界的信号且与数据D同步，一个时钟周期内10位的有效数据D，且高位在前。主要信息就这些了，信号FCO、DCO、D接入FPGA。
<!--more-->

## 方法1——利用官方LVDS_RX的IP核
简单的说下思路，由于程序均为并行，以下步骤也已并列形式给出。
* 将D和FCO信号引入LVDS_RX中，两位两位的读取，读取时钟为DCO。
* 使用一个11位的Buffer寄存器，在每个上升沿的同时不断的将LVDS_RX读取到的数据以移位的形式添加到最后。（注意这里是使用了11位Buffer，比数据长度多1，其用途可参考下方运行辅助理解）
* 在每个DCO的上升沿对LVDS_RX接收到的FCO进行打一拍处理
* 在每个DCO的上升沿对当前时刻接收到的2位FCO数据和前一个上升沿的数据（上述中打一拍）进行比较判定，若前一时刻为00，当前为11，则11位Buffer的[9:0]位接收到的数据；若前一时刻为01，则11位中Buffer的[10:1]为采集数据；其余条件Buffer保持。

这里最后一个处理中之所以有两种情况是因为LVDS_RX在读的过程中无法确保其开始位置，故这里将两种方法都进行考虑后进行综合。下图描述了LVDS_RX在读取时的两种可能的状态。
* **状态1**
![CASE1](http://o85gvbiad.bkt.clouddn.com/20161024-ad9212-lvds-case-1.png)
* **状态2**
![CASE2](http://o85gvbiad.bkt.clouddn.com/20161024-ad9212-lvds-case-2.png)

## 方法2——根据时序自行处理

同样简单的说一下思路，该方法对于10-bits ADC需要使用到一个12-bits的Buffer用于数据的缓存。
* DCO上升沿进行采样，数据依次存入Buffer[11,9,7,5,3,1]中。
* DCO下降沿进行采样，数据依次存于Buffer[10,8,6,4,2,0]中。
* 类似于上述方法对FCO一样双边沿采样存于一个Reg[3:0]中。
* 在Reg[3:0]==0011时，标志位置1。
* 在DCO的上升沿在标志位置于1的时候将Buffer中的[11:2]提取出来成为ADC采集到的数据。
* 根据需要添加FIFO进行数据同步。
这一部分后续再时序上可能不如方法1，后期可以通过时序约束进行优化，后续学习后再来添加补充。

**补充1**：注意在buffer[11:2]中数据提取时要注意是在DCO的哪个边沿进行提取的，一定要充分注意，并进行良好的时序约束！

希望对阅读的你有着帮助，欢迎探讨。如果有什么觉得不对的，一定不要客气的留言回复大力拍砖~