---
title: 原创 | Matlab之按位操作
date: 2016-11-10 10:47:34
categories:
  - Matlab
tags:
  - Matlab
---

在硬件语言Verilog中按位操作是相对容易的，在C语言中一样的用好逻辑符号“|”、“!”、“&”、“>>”等即可。但是在Matlab中一些类似的操作是判断或者逻辑用法，不能用在按位操作上。那么在其中就需要用到函数来进行操作了。

在此记录两种按位操作的方法：按位左右移**bitshift**,按位与**bitand**。

<!--more-->

## 按位左右移bitshift ##

```matlab
C = bitshift(A,K) returns the value of A shifted to the left by K bits, 
    where A is a signed or unsigned integer array. Shifting by K bits
    is the same as multiplication by 2^K. Negative values of K are allowed 
    and this corresponds to shifting to the right, or dividing by 2^ABS(K) 
    and rounding to the nearest integer towards negative infinity. If the 
    shift causes C to overflow the number of bits in the integer class of A, 
    then the overflowing bits are dropped.
 
    If A is a double array, then all elements must be non-negative integers
    less than or equal to intmax('uint64'), and bitshift 
    drops any bits overflowing 64 bits.
```
其中K为正表示向左移，K为负值表示向右移；示例如下有：
```matlab
>> bitshift(5,1)

ans =

    10

>> bitshift(5,-1)

ans =

     2

```
## 按位与bitand ##

```matlab
C = bitand(A,B) returns the bitwise AND of arguments A and B, 
    where A and B are signed or unsigned integer arrays. If A and B are
    double arrays, then they must contain non-negative integer elements
    less than or equal to intmax('uint64').
```
两个简单的示例如下：
```matlab
>> bitand(5,4)

ans =

     4

>> bitand(5,15)

ans =

     5
```

其他还有一些按位操作的函数，可以参考如下。

	See also 
	*bitor*, *bitxor*, *bitcmp*, *bitshift*, *bitset*, *bitget*, *intmax*.