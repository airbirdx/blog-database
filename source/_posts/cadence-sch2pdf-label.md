---
title: 整理 | Cadence 生成带有网络追踪的 PDF 原理图
date: 2017-01-04 21:14:56
categories:
  - HW
tags:
  - Cadence
  - PCB Design
---

在使用 Cadence 进行设计时，经常需要在原理图绘制完成后将其转换成PDF文件进行进一步的阅读查错或者交接。听说了可以生成带有网络追踪的 PDF（就是带有标签跳转）后，对其生成方法进行了探索整理，在此记录如下。

<!--more-->

## 软件准备
* **Cadence**：这个就没什么说的了吧，一切一切的基础。（本人使用版本16.6）
* **FreePDF**：PDF 制作使用，其实相当于一个虚拟打印机，可以将一些文本打印为 PDF 格式。下载地址为[FreePDF官网](http://freepdfxp.de/)。在安装完成后在设备和打印机中可以看到一个 FreePDF 的虚拟打印机。
* **Ghostscript**：Ghostscript 是一套建基于 Adobe、PostScript 及可移植文档格式（PDF）的页面描述语言等而编译成的免费软件。下载地址为[Ghostscript 官网](https://ghostscript.com/)，选择合适的版本下载即可。

## PDF 生成操作

### 流程图
下图展示了在 Capture 中 PDF 生成的流程，其中的 Postscript driver 就是上文中的 FreePDF，Postscript2PDF converter 就是上文中的 Ghostscript。

![PDF 生成流程](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20170104-capture-generate-pdf.png)

### 操作步骤

1. 在打开的 Capture 工程窗口，点击菜单栏 Accessories -->> Cadence Tcl/Tk Utilities -->> Utilities，进入一个 Application 窗口后选择 [Design Utilities] 选项下的 PDF Export 后，电子右侧的[Launch]按钮启动。如下图中所示。
![步骤图1](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20170104-capture-pdf-step-01.png)
![步骤图2](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20170104-capture-pdf-step-02.png)

2. 在 PDF Export 界面中，如下图所示。
![步骤图3](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20170104-capture-pdf-step-03.png)
	* (1)为输出文件的路径(2)为输出文件的名称，(1)和(2)请按照需求选择更改即可。
	* (3)处更改为 FreePDF
	* (4)处需要选择 Ghostscript 选项
	* (5)处方框中需要进行一定更改，比如我安装了 64 位，安装路径为 C:\Program Files\gs\...，那么需要把{}内的 `gswin32c.exe` 更改为 `C:\Program Files\gs\gs9.19\bin\gswin64c.exe`
	* Option部分保持默认即可，记得勾选`Create Net and Part Bookmarks`
	* Output Paper Size根据设定自行更改即可

3. 点击 [OK]，等待生成即可。

4. 打开生成的 PDF ，即可看到其书签目录等信息，另外 PDF 文件中的元件还可以点击查看其属性，生成效果见下图所示。
![步骤图4](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20170104-capture-pdf-step-04.png)
![步骤图5](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20170104-capture-pdf-step-05.png)

### 进一步改进
上述步骤 2 中讲到了需要更改 FreeFDP 和将 {} 内的 `gswin32c.exe` 更改为 `C:\Program Files\gs\gs9.19\bin\gswin64c.exe`，为了减少后续每次生成时的改动，我们可以直接改动默认的相关文本文件，使得点击选项后为正确的路径文件。

修改文件路径为：`<Installdirectory>:\tools\capture\tclscripts\capUtils`，比如我的为
`D:\Cadence\SPB_16.6\tools\capture\tclscripts\capUtils`。文件为`capPdfUtil.tcl`。

1. 将 `gswin32c.exe` 更改为正确路径
![步骤图6](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20170104-capture-pdf-step-06.png)
更改为
![步骤图7](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20170104-capture-pdf-step-07.png)

2. 将 PS 默认为 FreePDF
![步骤图8](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20170104-capture-pdf-step-08.png)
更改为
![步骤图9](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20170104-capture-pdf-step-09.png)

3. 保存后，再次打开 PDF Export，就可以见到默认已经变为了我们所更改的参数。

## 参考文章
[1] [FlowCAD_AN_Capture_PDF_Export.PDF](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/FlowCAD_AN_Capture_PDF_Export.pdf)
[2] [OrCAD_Capture_TclTk_Extensions.PDF](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/OrCAD_Capture_TclTk_Extensions.pdf)

注：本文系参考[1]的翻译文，根据自己风格进行适当调整，在此对原文表示感谢。[2]文可以安装 Everything 进行硬盘搜索，安装 Cadence 时已经自行安装在硬盘上了。