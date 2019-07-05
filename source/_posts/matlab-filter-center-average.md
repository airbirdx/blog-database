---
title: 整理 | Matlab之中心平滑滤波
date: 2016-12-22 20:37:10
categories:
  - Matlab
tags:
  - Matlab
---

滑动平均(moving average)：在地球物理异常图上，选定某一尺寸的窗口，将窗口内的所有异常值做算术平均，将平均值作为窗口中心点的异常值。按点距或线距移动窗口，重复此平均方法，直到对整幅图完成上述过程，这种过程称为滑动平均。

滑动平均相当于低通滤波，在重力勘探和测井资料处理解释中常用此方法。

如果滑动窗长为n的话，滑动平均就是让数据通过一个n点的FIR滤波器，滤波器抽头系数都是1，这样取滑动平均就是起到序列平滑的作用。

Matlab中有多种滑动平均方法，比如filter和tsmovavg方法都可以实现。

<!--more-->

## 普通滑动平均 ##
基于filter的普通无权重滑动平均，有关于filter函数，可以`doc filter`进行详细信息的查看，这里我们由于只使用了简单的滑动平均，在此记录一种简单的滑动平均方法。
```matlab
seqOriginal = rand(1,100);
windowSize  = x;
seqFilter   = filter( ones(1, windowSize) / windowSize, 1, seqOriginal );
```

上述命令实际计算的是：
```
x表示seqOriginal, y表示seqFilter, a表示windowSize。
y(1) = (1 / a) * x(1);
y(2) = (1 / a) * x(2) + (1 / a) * x(1);
...
y(a) = (1 / a) * x(a) + (1 / a) * x(a - 1) + ... + (1 / a) * x(1);
...
y(i) = (1 / a) * x(i) + (1 / a) * x(i - 1) + ... + (1 / a) * x(i - a + 1);
...
```

注：该方法由于是计算该点和之前windowSize的点的平均值，故其输出结果相对于原数据趋势有一个滞后。如果数据量比较少，可能影响较大。

## 中心滑动平均 ##
还有一种滑动平均的方法为中心滑动平均，数据点位于滑动窗的中心进行平均值的计算。则上述的计算变为（在此为了方便虚数，设a为奇数）:
```
y(1) = (1 / a) * x(1) + (1 / a) * x(2) + ... + (1 / a) * x((a+1) / 2);
y(2) = (1 / a) * x(1) + (1 / a) * x(2) + ... + (1 / a) * x((a+1) / 2 + 1);
...
y((a + 1) / 2) = (1 / a) * x(1) + (1 / a) * x(2) + ... + (1 / a) * x((a+1) / 2) + (1 / a) * x(a);
...
y(i) = (1 / a) * x(i - (a - 1) / 2) + (1 / a) * x(i - (a - 1) / 2 + 1) + ... + (1 / a) * x(i) + ... + (1 / a) * x(i + (a+1) / 2);
...
```

将上述式子转换为Matlab语句为：
```matlab
seqOriginal = rand(1,100);
windowSize  = x;
seq1        = filter( ones(1, windowSize / 2 + 1) / windowSize, 1, seqOriginal );
seq2        = filter( ones(1, windowSize / 2 + 1) / windowSize, 1, fliplr(seqOriginal) );
seqFilter   = seq1 + fliplr(seq2) - 1 / windowSize * seqOriginal;
```

为了方便使用，为其写了一个function函数用来调用。
```matlab
%fun_CenterAverageFilter
%--------------------------------------------------------------------------
%   seqFilter = fun_CenterAverageFilter(seqOriginal, windowSize)
%   中心滑动平均
%--------------------------------------------------------------------------
%   seqFilter   |Matrix|    滤波后输出序列  
%   seqOriginal |Matrix|    原始序列
%   windowSize  |Double|    滑动窗口
%--------------------------------------------------------------------------
%Author:    Liu Tong
%History:
%----------------------------------------
%Rev:  1.0
%Date: 2016/12/22
%   create.
%--------------------------------------------------------------------------
function seqFilter = fun_CenterAverageFilter(seqOriginal, windowSize)
seq1        = filter( ones(1, windowSize / 2 + 1) / windowSize, 1, seqOriginal );
seq2        = filter( ones(1, windowSize / 2 + 1) / windowSize, 1, fliplr(seqOriginal) );
seqFilter   = seq1 + fliplr(seq2) - 1 / windowSize * seqOriginal;
end
```
