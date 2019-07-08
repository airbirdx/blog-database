---
title: 整理 | S-Record数据格式解析
date: 2016-12-29 20:30:57
categories:
  - HW
tags:
  - HW
---

S-Reord是一种由摩托罗拉公司创建的文件格式（不得不说，摩托罗拉厉害啊，SPI和S-Record都是他们创造的）。S-Record的基本字符为ASCII字符，用以表示相应的十六进制数据。该数据格式还有以下的几种名字或缩写SRECORD, SREC, S19, S28, S37。S-Record格式多用在存储类芯片，Flash、EPROMs、EEPROMs等。

本文主要介绍S-Record格式及其各部分所代表的含义，更多详细的介绍可以看本文资料主要来源，[Wikipedia--SREC (file format)](https://en.wikipedia.org/wiki/SREC_%28file_format%29)。

<!--more-->

## S-Record格式详解

在维基百科上看到的这幅图把S-Record格式表达的十分完善，在此引用一下。
![Motorola S-record format ready reckoner](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20161229-Motorola-SREC-Chart.png)

**注意**：
* 此图中的每一个格子表示一个字符，其中在中间一条主格式下面的2 Bytes表示两个字符，其真实存储时为两个字符（一个字符的ASCII码为一个字节）。
* 在下方粉红色部分下的括号，16 bits表示的是一个方框中符号对应的二进制数。比如'F'就对应0xF(1111)。

S-Record数据按行进行存贮。其主要分为以下几个部分：
* **type**：类型，主要有S0-S3, S5, S7-S9等几种模式。
* **count**：长度，主要表示该部分之后有多少字节长度的数据（一个字节表示两个字符）。
* **address**：数据写入的起始地址，主要根据类型有着不同的地址长度，其采用big endian大端模式（高位在前）存储。
* **data**：数据，一行S-Record中的数据，其长度由type和count共同决定。可以按照如下方式进行计算（单位Byte）：< count > - < address >（取值为2、3、4） - 1（< checksum >字段的长度）
* **checksum**：校验和，用于校验整行数据是否正确。

该图中左下角部分表示了不同类型下地址区的长度和不同类型的数据格式。注意：纵观整幅图，含有数据的几种格式为S0-S3, S5，其他模式均无数据的存在。

## 示例

数据：**S1137AF00A0A0D0000000000000000000000000061**
拆解：**S1 - 13 - 7AF0 - 0A0A0D00000000000000000000000000 - 61**

1. 类型为**S1**
2. 长度为0x**13** = 19
3. 根据S1的数据格式，可以知道count后2 Bytes为address数据(**7AF0**)
4. 最后一个字节为校验位(**61**)
5. 剩余部分为数据位(**0A0A0D00000000000000000000000000**)

有关checksum校验的计算，还是以上述为例，
1. 相加，0x13 + 0x7A + 0xF0 + ... + 0x00 = 0x19E
2. 取后两个字节0x9E
3. 0xFF - 0x9E即可得到校验值0x61