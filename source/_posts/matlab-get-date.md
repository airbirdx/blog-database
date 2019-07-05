---
title: 原创 | Matlab获取当前时间信息
date: 2016-11-10 10:47:34
categories:
  - Matlab
tags:
  - Matlab
---

本文主要介绍下Matlab中如何获取当前时间的一些方法。

## 基本变量date、now、clock
1. date	按照**日期字符串**返回当前系统时间
2. now	按照**连续的日期数值**返回当前系统时间
3. clock按照**日期向量格式**返回当前系统时间

<!--more-->

	>> date, now, clock
	
	ans =
	
	15-May-2016
	
	
	ans =
	
	   7.3647e+05
	
	
	ans =
	
	   1.0e+03 *
	
	    2.0160    0.0050    0.0150    0.0170    0.0100    0.0195

## 使用year、month、day等函数获取

可以使用的获取函数有year,month,day,hour,minute,second，其作用是从第一部分讲到的字符串和连续型日期时间个时钟提取信息。

	>> [year(date), year(now)]
	
	ans =
	
	        2016        2016

但是，其没有办法从向量型日期中读取信息。

	>> year(clock)
	
	ans =
	
	     5     0     0     0     0     0

## 其他函数datestr等

还有一些日期转字符串的函数，比如datestr。

	>> datestr(date), datestr(now), datestr(clock)
	
	ans =
	
	15-May-2016
	
	
	ans =
	
	15-May-2016 17:20:03
	
	
	ans =
	
	15-May-2016 17:20:03

有关于datestr函数和其他相关类似的函数，可以通过`help datestr`或者`doc datestr`进行访问查看。以下为**摘取部分（有删减）**。

	>> help datestr
	 datestr String representation of date.
	 
	    S = datestr(D, F) converts one or more date vectors, serial date
	    numbers, or date strings D into the same number of date strings S.
	    Input argument F is a format number or string that determines the
	    format of the date string output. Valid values for F are given in Table
	    1, below. Input F may also contain a free-form date format string
	    consisting of format tokens as shown in Table 2, below. 
	 
	 	Table 1: Standard MATLAB Date format definitions
	 
	    Number           String                   Example
	    ===========================================================================
	       0             'dd-mmm-yyyy HH:MM:SS'   01-Mar-2000 15:45:17 
	       1             'dd-mmm-yyyy'            01-Mar-2000  
	       2             'mm/dd/yy'               03/01/00     
	       3             'mmm'                    Mar          
	       4             'm'                      M            
	       5             'mm'                     03            
	       6             'mm/dd'                  03/01        
	       7             'dd'                     01            
	       8             'ddd'                    Wed          
	       9             'd'                      W            
	      10             'yyyy'                   2000         
	      11             'yy'                     00           
	      12             'mmmyy'                  Mar00        
	      13             'HH:MM:SS'               15:45:17     
	      14             'HH:MM:SS PM'             3:45:17 PM  
	      15             'HH:MM'                  15:45        
	      16             'HH:MM PM'                3:45 PM     
	      17             'QQ-YY'                  Q1-96        
	      18             'QQ'                     Q1           
	      19             'dd/mm'                  01/03        
	      20             'dd/mm/yy'               01/03/00     
	      21             'mmm.dd,yyyy HH:MM:SS'   Mar.01,2000 15:45:17 
	      22             'mmm.dd,yyyy'            Mar.01,2000  
	      23             'mm/dd/yyyy'             03/01/2000 
	      24             'dd/mm/yyyy'             01/03/2000 
	      25             'yy/mm/dd'               00/03/01 
	      26             'yyyy/mm/dd'             2000/03/01 
	      27             'QQ-YYYY'                Q1-1996        
	      28             'mmmyyyy'                Mar2000        
	      29 (ISO 8601)  'yyyy-mm-dd'             2000-03-01
	      30 (ISO 8601)  'yyyymmddTHHMMSS'        20000301T154517 
	      31             'yyyy-mm-dd HH:MM:SS'    2000-03-01 15:45:17 
	 
	    Examples:
	 	datestr(now) returns '24-Jan-2003 11:58:15' for that particular date,
	 	on an US English locale datestr(now,2) returns 01/24/03, the same as
	 	for datestr(now,'mm/dd/yy') datestr(now,'dd.mm.yyyy') returns
	 	24.01.2003 To convert a non-standard date form into a standard MATLAB
	 	dateform, first convert the non-standard date form to a date number,
	 	using DATENUM, for example, 
	 	datestr(DATENUM('24.01.2003','dd.mm.yyyy'),2) returns 01/24/03.
	 
	 	See also date, datenum, datevec, datetick.
