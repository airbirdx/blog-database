---
title: 原创 | 从七牛云批量下载存储文件
date: 2018-04-21 16:47:33
categories:
  - Web
tags:
  - qiniu
---
前端之间因为换电脑转移 Blog 空间，在转移了博文后发现源图像文件夹未能转移并且已经删除了。就想着七牛云上还有副本，就想着从七牛云上下载下来，可是那么些图片文件一个个下载又很是麻烦，在网络上搜罗了一番方法说明，又去七牛官方看了点文档，最终使用官方提供 `qshell.exe` 完成存储文件的批量下载。

<!--more-->

## 下载 qshell

在[命令行工具(qshell) - 七牛开发者中心](https://developer.qiniu.com/kodo/tools/1302/qshell)根据需求下载最新版本命令行工具。作者系统为windows 10，使用时下载的为v2.1.5版本。主要使用到其中的[`account`](https://github.com/qiniu/qshell/blob/master/docs/account.md)和[`qdownload`](https://github.com/qiniu/qshell/blob/master/docs/qdownload.md)指令，具体使用方法可以点击链接仔细查询。在此对使用到部分做简单摘录。

## qshell配置账户

新建一文件夹，命名自定义。作者在此命名为 `downloadfiles`。

将开始下载的 `qshell.exe` 放在所创建的文件夹中。

在文件下夹 `Shift + 鼠标右键` 选择 `cmd` 或 `PowerShell` 打开命令行窗口。

以 `PowerShell` 为例，键入

```
.\qshell account <Your AccessKey> <Your SecretKey>
```

配置账户信息，其中AK与SK可以在七牛网[个人中心章节](https://portal.qiniu.com/user/key)中找到。

![七牛网个人中心](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20180423-qiniu-account-key.png)

设置完成后可以键入

```
.\qshell account
```

进行配置AK与SK的显示。

## 配置参数设置

在文件夹路径下新建 `qshell.conf` 文件，用来存储配置信息，文件格式如下。

```
{
    "dest_dir"      : "xxxx",
    "bucket"        : "xxxx",
    "cdn_domain"    : "http://xxxx.bkt.clouddn.com/",
    "prefix"        : "",
    "suffix"        : ".png"
}
```

其中各项可以再下载 qshell.exe 的界面中找到，在此只对所用到部分进行介绍，详细的还请参考官方文档。

| 参数名     | 描述                                                         | 可选参数 |
| ---------- | ------------------------------------------------------------ | -------- |
| dest_dir   | 本地数据备份路径，为全路径                                   | N        |
| bucket     | 空间名称                                                     | N        |
| prefix     | 只同步指定前缀的文件，默认为空                               | Y        |
| suffixes   | 只同步指定后缀的文件，默认为空                               | Y        |
| cdn_domain | 设置下载的CDN域名，默认为空表示从存储源站下载，【该功能默认需要计费，如果希望享受10G的免费流量，请自行设置cdn_domain参数，如不设置，需支付源站流量费用，无法减免！！！】 | N        |

**备注**：在Windows系统下面使用的时候，注意 `dest_dir` 的设置遵循 `D:\\jemy\\backup` 这种方式。也就是路径里面的 `\` 要有两个（`\\`）。

## qdownload指令下载

在命令行窗口输入

```
.\qshell qdownload 10 qshell.conf
```

进行所有存储空间中后缀为".png"文件的下载，10为下载线程数。

![qdownload](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20180423-qiniu-qdownload.png)

另，qdownload 指令的具体参数及定义描述如下所示。

```
qshell qdownload [<ThreadCount>] <LocalDownloadConfig>
```

| 参数名称            | 描述                                                         | 可选参数 | 取值范围                            |
| ------------------- | ------------------------------------------------------------ | -------- | ----------------------------------- |
| ThreadCount         | 下载的并发协程数量                                           | Y        | 1-2000，如果不在这个范围内，默认为5 |
| LocalDownloadConfig | 本地下载的配置文件，内容包括要下载的文件所在空间，文件前缀等信息，具体参考配置文件说明 | N        |                                     |