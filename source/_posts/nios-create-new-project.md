---
title: 原创 | 使用 NIOS 创建软核工程
date: 2018-06-06 14:15:10
categories:
  - FPGA
tags:
  - NIOS
---

本文主要介绍基于 Quartus + NIOS II 使用软核时如何创建软核工程并进行配置，最后可以生成 ELF 可下载文件，进行下载调试。

<!--more-->

## 打开 NIOS II 软件

1. 在开始菜单中选中 NIOS 程序，然后单击打开。

![1](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20180606-nios-config-bsp-editor.png)

2. 自定义配置好路径，在这里我配置为桌面上的 SW 文件夹。

![2](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20180606-nios-config-prj-a.png)

## 创建 Hello 例程

1. 点击`File->New->Nios II App.. and BSP from ..`创建一个新的工程。

![3](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20180606-nios-config-prj-b.png)

2. 选择 SOPC 文件路径，此文件位于 Quartus 工程中 MIOS IP 核文件夹下。

	[4](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20180606-nios-config-prj-properties	.png)

3. 输入工程文件名，本文中键入 `BDM` 为例。
4. 注意不勾选 `Use default location` 选项，点击右侧 `...` 按钮选择合适的路径，这样做的目的是将Quartus和NIOS的工程分开管理。
5. 在下方选择 `Hello World` 默认工程后，点击 `Next` 进入下一个页面。
6. 保持默认信息即可，确认无误后点击 `Finish` 完成此部分操作。

![5](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20180606-nios-config-properties-path-a.png)

7. 完成后的界面可以看到左侧有了相关的信息，然后双击 `hello_world.c` 可以在中心区域看到代码部分。

![6](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20180606-nios-config-properties-path-b.png)


## 补充完善代码

1. 如果只运行 Hello 的 DEMO 程序，无其他代码，直接进入下一大步骤。
2. 将代码以及头文件准备好，在此约定源文件置于 src 文件夹中，头文件置于 inc 文件夹中。
3. 将两个文件夹拷贝到工程文件夹下，在本实例中为 `BDM` 文件夹。

![7](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20180606-nios-copy-code.png)

4. 在NIOS软件中左侧栏选择 `Refresh` 进行刷新。可以看到刚才拷贝的文件夹已经在列表中了。

![8](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20180606-nios-delete-hello.png)

5. 在工程 `BDM` 上选中右键 `右键 -->> New -->> Source Folder`，分别添加名为 `inc` 和 `src` 的文件夹。

![9](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20180606-nios-main-window.png)

7. 如果 `src` 中有程序包含 `main` 函数，那么需要删去 `hello_world.c` 文件。

![10](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20180606-nios-new-bsp-prj.png)

## 配置 BSP Editor

1. 在左边列表中选择bsp工程，然后 `右键 -->> NIOS II -->> BSP Editor`，打开编辑框。

![11](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20180606-nios-new-hardware-app.png)

2. 根须需要进行选择，从上向下第一个框中的 `jtag` 或 `none` 表示是否启用 JTAG 模式，在调试时启用，运行 `Release` 版本时选择 `none`。勾选 `enable_small_c_lib...` 的选项，然后将`exception_stack_size` 设置为 10240。最后点击 `Generate` 运行生成即可。

![12](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20180606-nios-new-src-folder.png)

## 配置include路径

1. 选择含有 `main` 函数的C文件打开，在本实例中是 `BDM.c`。
2. 在菜单栏选择 `Project->Properties` 打开属性配置。

![13](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20180606-nios-open-bsp-editor.png)

3. 选择 `C/C++ General->Paths and ...`，然后在右侧空白区添加工作区或文件系统。主要为两个 Workspace 和三个 inc 路径。

![14](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20180606-nios-open-sw.png)

4. 选择 `Nios II App...->Nios II App... Paths`，在其中 include dir 区域添加三个 `inc` 文件夹的路径。

![15](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20180606-nios-refreash-tool.png)

5. 添加完成后点击 `OK` 完成此部分配置。

## 编译工程

1. 直接在菜单栏选择 `Project -->> Build All` 或者键盘 `Ctrl + B` 编译全工程。

2. 如果出错，可以将错误选中，然后右键将其手动删除，在左侧选中工程然后 `右键 -->> Index -->> Rebuild`，再编译几次尝试。NIOS II 会有些小 BUG。如果是都按照上述操作处理了，是可以正常编译通过无 Error 的。

##配置并下载 
1. 在工程上 `右键 -->> Run As -->> Nios II Hardware`或者在快捷栏选择进入下载配置界面。

![16](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20180606-nios-set-hardware-app.png)

2. 选择 `Target Connection` 子标签界面，然后如果有使用 USB-Blaster 连接到上电的电路板，点击 `Refresh Connection` 刷新链接，然后勾选下方的两个 `Ignore` 按钮，将会看到下方 `Run` 按钮可以点击，最后点击执行即可。


