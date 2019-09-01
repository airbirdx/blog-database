---
title: 原创 | 使用 Pandoc 实现 Markdown 文件转 PDF 文件
date: 2016-12-7 20:47:34
categories:
  - SW
tags:
  - Write
---

Markdown 写法简单明快，我十分喜欢，以至于我最近都想使用 Markdown 快速的进行测试说明书的写作，但是考虑到这文档是要进行交接的，一个 .md 的文件在内部传输还是有不便，于是就想到了能不能把 Markdown 转为 PDF 文件作为通用文件。

然后搜索后看到了这样的一篇文章[如何把 Markdown 文件转化为 PDF](http://www.zhihu.com/question/20849824)，文中提到了很多方法，有使用 `.md -->> .html -->> .pdf` 的，也有 `.md -->> .word -->> .pdf` 的，也有 `.md -->> .tex -->>.pdf` 的。最终考虑到之前曾经使用 LaTex 进行过文章写作，并且 PC 中还有着 LaTex 环境，决定**使用 Pandoc 实现 Markdown 转 PDF**。

<!--more-->

## Pandoc 介绍 ##

Pandoc 是一个用 haskell 编写的开源文本转换工具，小巧迅速且支持格式广泛，堪称文本转换应用的瑞士军刀。支持很多种输入输出，有关 Pandoc 可以在其[官网](http://pandoc.org/)进行详细了解。下载页面可以[点此进入](https://github.com/jgm/pandoc)，在其中选择合适的版本即可（GitHub 下载不多赘述）。

## Markdown 转 PDF ##

### 全英文文档转换 ###

在需要转换的文件路径下进行 `Shift+鼠标右键` 选择此处进入命令行，键入
```
pandoc input.md -o output.pdf
```
即可完成最简单的 PDF 文档。

### 中英文文档转换 ###

在编写时，由于我们主体还是中文，那么若文档中存在中文字符，那么转换就会出问题。为了使的其支持中文，我们需要使用 xelatex 编译器（有关 xelatex，还请大家自行搜索），下面直接放干货，可以一步操作到位的命令如下。

```
pandoc -N -s --toc --smart --latex-engine=xelatex -V CJKmainfont='黑体' -V mainfont='Times New Roman' -V geometry:margin=1in input.md -o output.pdf
```
大家可以自行编辑一些 `.md` 文档然后使用着条命令进行转换尝试。另外，Markdone 转 PDF 的操作，也可以几个 `.md` 文件整合成一个 PDF 文件，其命令如下。
```
pandoc -N -s --toc --smart --latex-engine=xelatex -V CJKmainfont='黑体' -V mainfont='Times New Roman' -V geometry:margin=1in in1.md in2.md ... -o output.pdf
```

### 语法介绍 ###

有兴趣的童鞋可以查看官方的HELP文档进行详细的了解，传送门：[Pandoc Demos & README](http://pandoc.org/demos.html)。

若是想重点了解下上文中所用到的一些参数及其意义可以看下面的一些说明。

```
--latex-engine=xelatex
	# 因为文档中有中文字符，使用 XeLaTex 引擎（必选项）
```

```
-N	# 根据标题自动分配标号（可选项）
	# H1 标题 #Title# 		  --> 1/2/3/4/...
	# H2 标题 ##Title## 	  --> 1.1/1.2/1.3/...
	# H3 标题 ###Title### 	--> 1.1.1/1.1.2/1.1.3/...
```

```
-toc	# 给PDF文件加上书签功能
```

有关这些命令的详细说明都可在上面提到的 [README](http://pandoc.org/demo/README) 中进行查阅。比如命令 `-V`，在上面操作中的作用就是设定中英文的显示字体，比如中文设定为黑体，英文设定为 `Times New Roman`，你也可以自行设定合适的字体。

```

`-V` *KEY*[`=`*VAL*], `--variable=`*KEY*[`:`*VAL*]

:   Set the template variable *KEY* to the value *VAL* when rendering the
    document in standalone mode. This is generally only useful when the
    `--template` option is used to specify a custom template, since
    pandoc automatically sets the variables used in the default
    templates.  If no *VAL* is specified, the key will be given the
    value `true`.
```

## 转换效果 ##

本文也对一些`.md`文件进行了 PDF 文件转换，并附一些效果图于后供大家参考。其中使用的 `input.md` 文件使用了[Cmd Markdown 简明说明书](https://www.zybuluo.com/mdeditor?url=https://www.zybuluo.com/static/editor/md-help.markdown#)的源文件，其网页渲染效果[点此可见](https://www.zybuluo.com/ghosert/note/2)，可以与生成的 PDF 进行一个对比，看 PDF 生成的效果如何。本文使用的 `input.md` 也放出[下载链接](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20160608-pandoc-md2pdf-input.md)，

![Page1](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20160608-pandoc-md2pdf-output_01.png)

![Page2](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20160608-pandoc-md2pdf-output_02.png)

![Page3](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20160608-pandoc-md2pdf-output_03.png)

![Page4](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20160608-pandoc-md2pdf-output_04.png)

![Page5](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20160608-pandoc-md2pdf-output_05.png)

![Page6](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20160608-pandoc-md2pdf-output_06.png)

![Page7](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20160608-pandoc-md2pdf-output_07.png)

