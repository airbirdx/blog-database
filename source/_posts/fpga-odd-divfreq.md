---
title: 原创 | FPGA 实现任意时钟分频
date: 2016-11-10 16:47:34
categories:
  - FPGA
tags:
  - FPGA
---

有时在基本模块的设计中常常会使用到时钟分频，时钟的偶分频相对奇分频来说比较简单易于理解，但是奇分频的理念想透彻后也是十分简单的，本文就针对奇分频做一个记录并列出了 modelsim 的仿真结果。

<!--more-->

## 奇分频

其实现很简单，主要为使用两个计数模块分别计数，得到两个波形进行基本与或操作完成。一个 5 分频的参考代码部分如下。

```verilog
module  div_freq(
	iCLK,
	iRST_n,
	oCLK
);
 
input   wire    iCLK;
input   wire    iRST_n;
output          oCLK;
 
parameter   N = 4'd5;
 
reg         clk_p;
reg [3:0]   cnt_p;
always @ (posedge iCLK or negedge iRST_n) begin
    if (!iRST_n)
        cnt_p <= 4'd0;
    else if (cnt_p == N - 1)
        cnt_p <= 4'd0;
    else
        cnt_p <= cnt_p + 1'b1;
end
always @ (posedge iCLK or negedge iRST_n) begin
    if (!iRST_n)
        clk_p <= 1'b0;
    else if (cnt_p == (N - 1) / 2)
        clk_p <= ~clk_p;
    else if (cnt_p == N - 1)
        clk_p <= ~clk_p;
    else
        clk_p <= clk_p;
end
 
 
reg         clk_n;
reg [3:0]   cnt_n;
always @ (negedge iCLK or negedge iRST_n) begin
    if (!iRST_n)
        cnt_n <= 4'd0;
    else if (cnt_n == N - 1)
        cnt_n <= 4'd0;
    else
        cnt_n <= cnt_n + 1'b1;
end
always @ (negedge iCLK or negedge iRST_n) begin
    if (!iRST_n)
        clk_n <= 1'b0;
    else if (cnt_n == (N - 1) / 2)
        clk_n <= ~clk_n;
    else if (cnt_n == N - 1)
        clk_n <= ~clk_n;
    else
        clk_n <= clk_n;
end
 
assign  oCLK = clk_p | clk_n;
 
endmodule

```

之后使用 Modelsim 仿真得到的结果如下图

![Modelsim仿真](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20160601-fpga-odd-divfreq.png)

## 小结

从仿真的结果中可以看到其已经实现了奇分频的功能，其中的分频倍数可以根据需要自行调整，不过感觉在实际需求中大多用到的也都是偶分频，奇分频不常见，但是深入理解了其实现机制对FPGA还是有一定的帮助作用的。

