---
title: 原创 | 利用 bat 脚本进行 QuartusII 和 NiosII 程序的下载
date: 2017-06-25 21:21:28

categories:
  - Quartus
tags:
  - Quartus
  - Nios
---

本文主要介绍了一种使用 bat 批处理调用脚本对 Altera 系列 FPGA 外挂 EPCS 芯片进行 SOF（QuartusII）和 ELF(NiosII) 程序的下载方法。

<!--more-->

## 事出必有因

当前固件程序存在 NIOS 软核部分，所以在调试测试以及生产的时候经常需要同时打开 QuartusII 和 NiosII 进行程序的更替下载，操作繁琐费时，于是就想到使用 Quartus 中的 Command-Line 来进行程序的下载。

软件环境：QuartusII & NiosII 15.1.0.185。

## 知其然

完成后的bat在双击后运行如下图所示，有 3 个选项可供选择。

![下载选项界面](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20170626-quartus-bat-download-results.png)

[0] 运行Altera Nios2 Command Shell
* 选择此项后将会正常进入到 Altera Nios2 Command Shell 命令行界面

[1] 执行在线下载功能
* 选择此项后将会进行程序的在线下载（并不会固化），而后进入调试模式运行，可以输出可能有的反馈信息

[2] 执行程序固化功能
* 选择此项后将会进行程序的固化操作，并在固化完成后让程序从基地址开始运行

## 知其所以然

能这么做完全是因为 Quartus 留出了相应的命令行接口，其实我们所使用的图形界面在后台也是转化为一个个的命令依次执行的。当前完成的工作也只是初步的完成了脚本实现，且需要一定的先决配置条件，后期仍有很大的改善空间，好好的学习一下 shell 脚本后应该可以使得步骤更为简化。

Step 1 : 编写程序下载脚本文件(\*.sh)
Step 2 : 编写 bat 文件调用 `Nios2 Command Shell` 并执行步骤1中的脚本文件

为了最快的完成此部分功能的开发，在 shell 脚本基础较少的情况下以上两个步骤通过更改 Quartus 安装路径下 `altera\15.1\nios2eds` 的 `Nios II Command Shell.bat` 和 `nios2_command_shell.sh` 文件来完成。**强烈建议对原文件进行备份后操作，下文中步骤也是对备份文件的更改。**

其中，
nios2_command_shell.sh 为 Nios II Command Shell 的运行脚本文件。

Nios II Command Shell.bat 为 bat 脚本运行文件，windows 环境下双击运行后即可调用 `nios2_command_shell.sh` 后进入 Nios II Command Shell。

另外，在以下内容中，设定 Example.sof 和 Example.elf 为演示下载用 SOF 和 ELF 文件名。

### sh脚本的更改

**注意：此文件应在路径 `altera\15.1\nios2eds` 下。**

* 将备份的 `nios2_command_shell.sh` 更改为方便自己使用的文件名，这里更改为 `example_sh.sh`。
* 找到以下区域

```bash
if [ -n "$*" ]; then
    exec $@
else
    echo "------------------------------------------------"
    echo "Altera Nios2 Command Shell [GCC 4]"
    echo
    echo "Version 15.1, Build 185"
    echo "------------------------------------------------"

    # Use bash --norc to get a clean shell
    # Use bash --rcfile <bashrc> to for a user rcfile
    # Default to using ~/.bashrc
    bash
fi
```

* 在`# Use bash --norc to get a clean shell`这一行前，也就是 `bash` 命令前添加以下内容。


```bash
########################################################
# 选择窗口 											   #
########################################################
echo " "
echo "[0] Run Nios2 Bash"
echo "[1] Run Test Program"
echo "[2] Download Normal Program"
echo " "

read -p "Please select : " SelNum
echo "------------------------------------------------"
echo " "

case ${SelNum} in
    0)
        echo "You select [0] Run Nios2 Bash"
        echo "Nios2 Command Line Is Running Now..."
        ;;
    1)
        ################################################
        # 在线下载
        ################################################
        echo "You select [1] Run Test Program"
        ################################################
        # 设置文件存储路径及SOF & ELF文件名
        PGM_PATH="C:/Users/Admin/Desktop/Program"
        SOF_FILE="Example.sof"
        ELF_FILE="Example.elf"
        ################################################
        echo " "
        echo "Program Information"
        echo "------------------------------------------------"
        echo "Program File Path	: ${PGM_PATH}"
        echo "SOF File		: ${SOF_FILE}"
        echo "ELF File		: ${ELF_FILE}"
        echo "------------------------------------------------"
        echo " "

        read -n 1 -p "Press any key to continue..."
        echo " "

        cd ${PGM_PATH}
        echo "Running Now..."

        # 执行在线下载命令，DEBUG模式
        nios2-configure-sof ${SOF_FILE}
        nios2-download ${ELF_FILE} -c USB-Blaster[USB-0] -r -g
        nios2-terminal -c USB-Blaster[USB-0]
        ;;
    2)
        ################################################
        # 程序固化
        ################################################
        echo "You select [2] Download Normal Program"
        ################################################
        # 设置文件存储路径及SOF & ELF文件名
        PGM_PATH="C:/Users/Admin/Desktop/Program"
        SOF_FILE="Example.sof"
        ELF_FILE="Example.elf"
        ################################################
        echo " "
        echo "Program Information"
        echo "------------------------------------------------"
        echo "Program File Path	: ${PGM_PATH}"
        echo "SOF File		: ${SOF_FILE}"
        echo "ELF File		: ${ELF_FILE}"
        echo "------------------------------------------------"
        echo " "

        read -n 1 -p "Press any key to continue..."
        echo " "

        cd ${PGM_PATH}
        echo "Running Now..."

        # SOF & ELF --> FLASH
        sof2flash --input=${SOF_FILE} --output="sw.flash" --epcs
        echo "sof2flash successfully!"
        elf2flash --input=${ELF_FILE} --output="hw.flash" --epcs --after="sw.flash"
        echo "elf2flash successfully!"
        echo " "

        # -b/--base <address>         Base address of FLASH/EPCS to operate on
        # -s/--sidp <address>         Base-address of System ID peripheral on target
        # -I/--id <system-id-value>   Unique ID code for target system
        ################################################
        # 设置下载使用的一些变量（仅限工程师进行修改）
        C_BASE=0x0
        C_SIDP=0x2A40
        C_ID=0x0
        ################################################

        nios2-configure-sof ${SOF_FILE}
        nios2-flash-programmer "sw.flash" --base=${C_BASE} --epcs --sidp=${C_SIDP} --id=${C_ID} --accept-bad-sysid --device=1 --instance=0 '--cable=USB-Blaster on localhost [USB-0]' --program 

        nios2-configure-sof ${SOF_FILE}
        nios2-flash-programmer "hw.flash" --base=${C_BASE} --epcs --sidp=${C_SIDP} --id=${C_ID} --accept-bad-sysid --device=1 --instance=0 '--cable=USB-Blaster on localhost [USB-0]' --program --go 

        echo " "
        echo "Program download successfully!"
        read -n 1 -p "Press any key to close this window..."
        exit
        ;;
    *)
        echo "Nios2 Command Line Is Running Now..."
        ;;

```

### bat文件的更改

**注意：此文件应在路径 `altera\15.1\nios2eds` 下。**

* 将备份的 `Nios II Command Shell.bat` 更改为方便自己使用的文件名，这里更改为 `example_bat.bat` 。
* 找到以下两行

```dos
:run_nios2_command_shell
@ "%_QUARTUS_BIN%\cygwin\bin\bash.exe" -c '%_NIOS2EDS_ROOT%nios2_command_shell.sh %*'
```
* 将其中的 `nios2_command_shell.sh` 更改为你自己的sh文件,此处更改为 `example_sh.sh`

### 简单说明
**备注：有关命令的一些功能介绍，大部分可以在 command line 中在命令后跟上 `--help` 进行查阅**.如下所示。
```bash
nios2-configure-sof --help
```

* `nios2-configure-sof`表示sof下载，其后台调用quartus_pgm将sof进行文件下载，等价于如下图形界面下的红框中操作。
	![quartus_pgm等效](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20170626-quartus-bat-download-equivalence-quartus_pgm.png)
* `nios2-download`表示elf在线下载，等价于等价于如下图形界面下的红框中操作。
	![nios2-download等效](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20170626-quartus-bat-download-equivalence-nios2-download.png)
* `nios2-terminal`表示进入调试模式，此时下载进去的程序才会运行，同时命令行窗口还将会显示和NiosII软件中一致的信息。
* `sof2flash`表示将sof文件转换成S-Record格式的flash文件，方便下载。
* `elf2flash`表示将sof文件转换成S-Record格式的flash文件，这里需要注意生成时需要加上`--after sw.flash`，表示elf程序的地址信息从sof之后开始。
* `nios2-flash-programmer`表示固化程序，其后可以接的参数代表含义可--help查看。这里只介绍下上面脚本中所用到的。
	* `--base`表示Qsys中EPCS模块的起始地址
	* `--epcs`表示下载的操作对象为EPCS系列芯片
	* `--sidp`表示Qsys中SystemID模块的起始地址
	* `--accept-bad-sysid`表示忽略System ID和System Timestamp
	* `--program`表示下载操作
	* `--go`表示从起始地址开始运行


## 下学而上达，循序渐进

[1] [Quartus II Scripting Reference Manual](https://www.altera.com/content/dam/altera-www/global/en_US/pdfs/literature/manual/tclscriptrefmnl.pdf)
[2] [Nios II Flash Programmer User Guide](https://www.altera.com/content/dam/altera-www/global/en_US/pdfs/literature/ug/ug_nios2_flash_programmer.pdf)
[3] [Nios II Command-Line Tools](https://www.altera.com/en_US/pdfs/literature/hb/nios2/edh_ed51004.pdf)
[4] [Command Line Scripting 2](https://www.altera.com.cn/zh_CN/pdfs/literature/hb/qts/qts_qii52002.pdf)







