---
title: 原创 | Matlab 生成随机数
date: 2016-11-10 11:42:34
categories:
  - Matlab
tags:
  - Matlab
---
Matlab 中有着丰富的随机数生成函数以应用于不同的情景，我一般使用生成随机的 1~N 的整数，但是之前了解的只有 **rand** 函数，其生成主要为 0 ~ 1 之间的随机数，但是和所预想的有差异。在此进行进行了help 指令，之后了解到了 **randi** 函数，并初步学会使用，在此做一个记录。

<!--more-->

## rand 函数

rand 函数是生产 0 ~ 1 的随机数，rand(N) 为生产一个 N 行 N 列的随机数矩阵，rand(M, N) 为生成一个 M 行 N 列的随机数矩阵。以下为一些示例。

	>> rand(3)
	
	ans =
	
	    0.8147    0.9134    0.2785
	    0.9058    0.6324    0.5469
	    0.1270    0.0975    0.9575
	
	>> rand(2, 3)
	
	ans =
	
	    0.9649    0.9706    0.4854
	    0.1576    0.9572    0.8003

在 help rand 后，我们可以观察其解释说明。

	>> help rand
	 rand Uniformly distributed pseudorandom numbers.
	    R = rand(N) returns an N-by-N matrix containing pseudorandom values drawn
	    from the standard uniform distribution on the open interval(0,1).  rand(M,N)
	    or rand([M,N]) returns an M-by-N matrix.  rand(M,N,P,...) or
	    rand([M,N,P,...]) returns an M-by-N-by-P-by-... array.  rand returns a
	    scalar.  rand(SIZE(A)) returns an array the same size as A.
	 
	    Note: The size inputs M, N, P, ... should be nonnegative integers.
	    Negative integers are treated as 0.
	 
	    R = rand(..., 'double') or R = rand(..., 'single') returns an array of
	    uniform values of the specified class.
	 
	    The sequence of numbers produced by rand is determined by the settings of
	    the uniform random number generator that underlies rand, RANDI, and RANDN.
	    Control that shared random number generator using RNG.

通过最后其提示的 See also, 我们可以观看其他和随机数有关的函数，看有没有合适的函数。

	    See also randi, randn, rng, RandStream, RandStream/rand,
	             sprand, sprandn, randperm.

## randi 函数

产生 1 ~ NUM 的随机整数，NUM 可调整。其中 NUM 作为一个输入的参数。randi(MAX, N) 产生一个最大值为 MAX 的 N 行 N 列的整数矩阵，randi(MAX, M, N) 产生一个最大值为 MAX 的 M 行 N 列的整数矩阵。以下为一些示例。

	>> randi(5, 6)
	
	ans =
	
	     1     1     5     3     1     1
	     2     5     2     1     2     4
	     1     5     1     1     2     4
	     1     3     4     5     5     4
	     2     3     2     5     1     3
	     3     2     2     3     1     3
	
	>> randi(5, 3, 9)
	
	ans =
	
	     2     4     4     5     3     3     4     5     5
	     4     1     4     4     3     3     4     3     5
	     1     2     1     3     2     5     2     2     3

在 help randi 后，我们可以观察其解释说明。

	>> help randi
	 randi Pseudorandom integers from a uniform discrete distribution.
	    R = randi(IMAX,N) returns an N-by-N matrix containing pseudorandom
	    integer values drawn from the discrete uniform distribution on 1:IMAX.
	    randi(IMAX,M,N) or randi(IMAX,[M,N]) returns an M-by-N matrix.
	    randi(IMAX,M,N,P,...) or randi(IMAX,[M,N,P,...]) returns an
	    M-by-N-by-P-by-... array.  randi(IMAX) returns a scalar.
	    randi(IMAX,SIZE(A)) returns an array the same size as A.
	 
	    R = randi([IMIN,IMAX],...) returns an array containing integer
	    values drawn from the discrete uniform distribution on IMIN:IMAX.
	 
	    Note: The size inputs M, N, P, ... should be nonnegative integers.
	    Negative integers are treated as 0.
	 
	    R = randi(..., CLASSNAME) returns an array of integer values of class
	    CLASSNAME.
	 
	    The arrays returned by randi may contain repeated integer values.  This
	    is sometimes referred to as sampling with replacement.  To get unique
	    integer values, sometimes referred to as sampling without replacement,
	    use RANDPERM.
	 
	    The sequence of numbers produced by randi is determined by the settings of
	    the uniform random number generator that underlies RAND, RANDN, and randi.
	    randi uses one uniform random value to create each integer random value.
	    Control that shared random number generator using RNG.