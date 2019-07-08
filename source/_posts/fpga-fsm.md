---
title: 整理 | FSM有限状态机
date: 2017-09-17 21:55:55
categories:
  - FPGA
tags:
  - FPGA
---

## 概述--何为有限状态机FSM

有限状态机-Finite State Machine，简写为FSM，是表示有限个状态及在这些状态之间的转移和动作等行为的数学模型，在计算机领域有着广泛的应用。通常FSM包含几个要素：状态的管理、状态的监控、状态的触发、状态触发后引发的动作。

以下为wiki上有关FSM的介绍，链接地址为[Finite State Machine-WiKi](https://en.wikipedia.org/wiki/Finite-state_machine)。

A **finite-state machine (FSM)** or **finite-state automaton** (plural: automata), or simply a **state machine**, is a mathematical model of computation used to design both computer programs and sequential logic circuits. It is conceived as an abstract machine that can be in one of a finite number of states. The machine is in only one state at a time; the state it is in at any given time is called the current state. It can change from one state to another when initiated by a triggering event or condition; this is called a transition. A particular FSM is defined by a list of its states, and the triggering condition for each transition.

<!--more-->

## FSM的两种形式

对于FPGA硬件电路，不管状态机是何种，我们假定F是当前状态和输入信号的函数。状态机的输出是由输出组合逻辑G提供的，G也是当前状态和输入信号的函数。那么对于状态机的逻辑，可以表达如下：
```
下一个状态 = F(当前状态，输入信号);
输出信号   = G(当前状态，输入信号);
```

在状态机中，我们依据状态机输出与输入的关系将状态机分为了两个模型，分别是Mealy状态机和Moore状态机。下面对这两个部分进行详解。

### Moore状态机

**Moore状态机**是**时序逻辑输出只取决于当前状态**的这一类状态机。此时，其输出表达式为`输出信号 = G(当前状态，输入信号);`这种。

时钟同步的Moore状态机结构如下图所示，从图中可以看出其输出逻辑G的输出仅由当前状态决定。

![时钟同步的Moore状态机结构](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20170917-fpga-fsm-moore-introduction.png)

### Mealy状态机

**Mealy状态机**是**时序逻辑输出不但取决于状态，还取决于输入**的一类状态机。此时，其状态机输出表达式为`输出信号 = G(当前状态，输入信号);`这种。

时钟同步的Mealy状态机结构如下图所示，从图中可以看出其输出逻辑G的输出由输入和当前状态一同决定。

![时钟同步的Mealy状态机结构](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20170917-fpga-fsm-mealy-introduction.png)

### Moore vs Mealy 状态机
1. Mealy机比Moore机“响应”速度快。

	Mealy机的输出与当前状态和输入有关，而Moore机输出仅与当前状态有关。Mealy机的输入立即反应在当前周期；Moore机的输入影响下一状态，通过下一状态影响输出。为此Mealy机比Moore机输出序列超前一个周期，即“响应速度”较快。Mealy机的输出在当前周期，具有较长的路径（组合逻辑）；Moore机的输出具有一个周期的延时，容易利用时钟同步，Moore机具有较好的时序。

2. Mealy机状态少，Moore机结构简单。

	由于Moore机的输出只有当前的状态有关，一个状态对应一个输出，Moore机具有更多的状态。Mealy和Moore机之间可以相互转化，对于每个Mealy机，都有一个等价的Moore机，Moore机状态的上限为所对应的Mealy机状态的数量和输出数量的乘积。

3. 状态机的状态通过触发器的数量来反应，Mealy机具有较少的状态，为此具有较少的触发器。

### Mealy和Moore状态机的互换

对于给定的时序逻辑功能，可以用Mealy机实现，也可以用Moore机实现。根据Moore机比Mealy机输出落后一个周期的特性，可以实现两种状态机之间的转换。把Moore机转换为Mealy机的办法为，把次态的输出修改为对应现态的输出，同时合并一些具有等价性能的状态。把Mealy机转换为Moore机的办法是，把当前态的输出修改为对应次态的输出，同时添加一些状态。如下图所示，为把Mealy机状态图转化为Moore机状态图。

![Mealy型机转换为Moore型机](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20170917-fpga-fsm-mealy-moore-translation.png)

如上图所示，把Mealy型机转换为Moore型机，只要把现时输出改变为下一时刻输出。对于状态A，有4个箭头指向它，表示在当前状态下有4个状态可以转换为下一状态的A；同时当前输出均为0，可以把0移入状态A内部，表示在Moore机中状态A的输出为0。同理，可以把0分别移位B/C状态。但对于状态D，有两个箭头指向且具有不同的输出值，需要把状态D分解成两个状态D1和D2（每个状态对应一个输出，当输出不同需要利用不同的状态表示，这即是Moore机具有更多状态的原因），得到完整的Moore机状态模型。

同理，若把上图的Moore机转换为Mealy机，只要把Moore机中下一状态的输出改变成Mealy机中当前状态的输出，由于D1/D2两状态处于A/C两状态之间，且相当于A/C节点之间的一个等效节点，可以把D1/D2两状态合并为一个状态。

### 状态机设计原则

Mealy机和Moore机实现的电路是同步时序逻辑电路的两种不同形式，它们之间不存在功能上的差异，并可以相互转换。Moore型电路有稳定的输出序列，而Mealy型电路的输出序列早Moore型电路一个时钟周期产生。在时序设计时，根据实际需要，结合两种电路的特性选择。

对于时序电路中常见的计数器，因计数器状态已经固定不变，无论采用Mealy型还是Moore型电路，复杂度一样。

在时序电路设计中Mealy型和Moore型电路的选择原则是：**当要求输出对输入快速响应及希望电路尽量简单时，选择Mealy型电路。当要求时序输出稳定，能接受输出序列晚一个周期，及选择Moore型电路不增加电路复杂性时，适宜选择Moore型电路。**

## Moore状态机

### 3段式状态机（推荐）

#### A-普通型

![三段式状态机-A](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20170917-fpga-fsm-moore-3-part-standard-a.png)

```verilog
// 第一个always块，描述当前状态的状态寄存器，non-blocking
always @ (posedge clk or negedge rst_n)    begin
    if (!rst_n)
        curr_state    <= idle;
    else
        curr_state    <= next_state;
end

// 第二个always块，描述状态转移，即下一状态的状态寄存器，blocking
always @ (*)    begin
    next_state    = idle;    // 初始化
    case (curr_state)
        idle:    begin
            if (...)
                next_state    = sx;
            else
                next_state    = sy;
        end
        ...
        default:
            next_state    = sz;
    endcase
end

// 第三个always块，组合逻辑描述输出，blocking
always @ (*)    begin
    if (!rst_n)    begin
        o1    = 1'b0;
    end
    else    begin
        case (curr_state)
            s1:    begin
                o1 = 1'b1;
            end
            ...
            default:    begin
                o1    = 1'b0;
            end
        endcase
    end
end

```
#### B-改良型

![三段式状态机-B](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20170917-fpga-fsm-moore-3-part-standard-b.png)

```verilog
// 第三个always块，时序逻辑描述输出，non-blocking
// 此时为时序逻辑
always @ (posedge clk or negedge rst_n)    begin
    if (!rst_n)    begin
        o1    <= 1'b0;
    end
    else    begin
        case (curr_state)	// 注意此处为当前状态
            s1:    begin
                o1	<= 1'b1;
            end
            ...
            default:    begin
                o1	<= 1'b0;
            end
        endcase
    end
end

```

#### C-改良型

![三段式状态机-C](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20170917-fpga-fsm-moore-3-part-standard-c.png)

```verilog
// 第三个always块，时序逻辑描述输出，non-blocking
// 此时为时序逻辑
always @ (posedge clk or negedge rst_n)    begin
    if (!rst_n)    begin
        o1    <= 1'b0;
    end
    else    begin
        case (next_state)	// 注意此处为前一状态
            s1:    begin
                o1	<= 1'b1;
            end
            ...
            default:    begin
                o1	<= 1'b0;
            end
        endcase
    end
end

```


## 参考感谢

[1] [两种类型状态机](http://blog.163.com/enjoy_yourself_ok/blog/static/1645812142012227102738745/)