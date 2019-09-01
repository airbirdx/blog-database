---
title: 原创 | Matlab 之 GUI 生成 EXE 文件
date: 2016-11-10 10:47:34
categories:
  - Matlab
tags:
  - Matlab
---

近期因为项目需要，简化流程，写了一些 Matlab 程序，并配备上了 GUI 界面使其简单易用。然后问题来了，**可移植性**。使用 Matlab 生成 EXE 文件（可以封装很多的 function），然后在一台安装有 Matlab Runtime 环境的电脑上运行，是一种不错的选择。

本文主要就我自己在 GUI 生成 EXE 文件上遇到的一些问题以及解决办法进行一个说明，希望可以帮助到有同样需求的人。

<!--more-->

## 配置环境 ##

* Windows 10系统
* Matlab 2013a
* Visual Studio 2013

## 配置方法 ##

打开 Matlab，在命令行中输入
```matlab
mbuild -setup
```
进行编译环境的配置，将会出现如下的界面。
```
Welcome to mbuild -setup.  This utility will help you set up  
a default compiler.  For a list of supported compilers, see  
http://www.mathworks.com/support/compilers/R2013a/win64.html 
 
Please choose your compiler for building shared libraries or COM components: 
 
Would you like mbuild to locate installed compilers [y]/n? 
```
输入 `y` 确认后观察是否有编译器的存在，我的一开始是没有的，如果你的有 matlab 自带的 lcc，那么幸运的是，你不用麻烦安装别的编译器了，这个已经足够，可以搜索与之相关的文章了；不幸的是后面的可能就不适合你了，因为我最后是使用的 VS 的编译器环境。

如果你也没有任何的编译器，那么很好，可以接着和我操作了，输入 `Ctrl + C` 退出当前命令，然后重新输入 `mbuild -setup`。选择 `n`，可以看到，出现了如下的一些选项。
```
Select a compiler: 
[1] Microsoft Software Development Kit (SDK) 7.1 
[2] Microsoft Visual C++ 2008 SP1 
[3] Microsoft Visual C++ 2010 
[4] Microsoft Visual C++ 2012 
 
[0] None 
```
Matlab 2013a 中居然没有我安装的VS2013，伤心。不过想来也是，没有是正常的，那么后续怎么办呢，按照其中的安装呗，2008SP1，2010, 2012 都可以。博主在这里选择了 VS2010，同一个电脑是可以安装不同版本的 VS 哦。

在 VS2010 完成后，重新启动 Matlab，然后再次输入这条指令 `mbuild -setup`，但是这次我们选择 `y`，进入如下的界面，这次就可以看到我们安装的 VS2010 环境了，Nice！然后一路正常设置就好。
```
Would you like mbuild to locate installed compilers [y]/n? y
 
Select a compiler: 
[1] Microsoft Visual C++ 2010 in D:\Program Files (x86)\Microsoft Visual Studio 10.0 
 
[0] None 
 
Compiler: 1
 
Please verify your choices: 
 
Compiler: Microsoft Visual C++ 2010  
Location: D:\Program Files (x86)\Microsoft Visual Studio 10.0 
 
Are these correct [y]/n? y
 
**************************************************************************** 
  Warning: Applications/components generated using Microsoft Visual C++      
           2010 require that the Microsoft Visual Studio 2010 run-time       
           libraries be available on the computer used for deployment.       
           To redistribute your applications/components, be sure that the    
           deployment machine has these run-time libraries.                  
**************************************************************************** 
 
 
Trying to update options file: C:\Users\AirBird\AppData\Roaming\MathWorks\MATLAB\R2013a\compopts.bat 
From template:              D:\Program Files\MATLAB\R2013a\bin\win64\mbuildopts\msvc100compp.bat 
 
Done . . . 
```

至此，Matlab 编译器配置完成。

## 生成EXE文件 ##

在命令行中键入如下命令可以进行 EXE 文件的生成。

```matlab
mcc -m myfile.m;		          % 只有 .m 文件时
mcc -m myfile.fig myfile.m;		% .fig 文件和 .m 文件一起时 
```

但是，在运行生成的 EXE 文件时我们会发现有黑框的存在，这个黑框其实是作为控制台的存在，有什么信息可以打印到上面。但是很多时候我们在运行的时候不希望黑框的生成，那么该如何操作呢？这里只需要更改下命令就可以了，如下。
```matlab
mcc -e myfile.m;		          % 只有 .m 文件时
mcc -e myfile.fig myfile.m;		% .fig 文件和 .m 文件一起时 
```
其中 `-e` 是生成**不带黑框的 EXE 程序**，是不是很神奇。但是这里需要注意的是，**`-e` 的用法只适合 VS 的引擎**。有关 mcc 的用法，可以 `help mcc` 或者 `doc mcc` 进行查阅。本文摘抄部分信息如下。
```
e Macro that generates a C Windows application on the Windows platform. On  
      non-Windows platforms, it is the same as the macro -m. This is  
      equivalent to the options "-W WinMain -T link:exe", which can be found  
      in the file <MATLAB>/toolbox/compiler/bundles/macro_option_e.    

```

![mcc -e](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20160609-matlab-gui2exe-mcce.png)