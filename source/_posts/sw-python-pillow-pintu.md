---
title: 原创 | 使用Python + Pillow完成图片墙拼图
date: 2018-5-3 17:42:00
categories:
  - Python
tags:
  - Pillow
---

因为脑子里的一些想法，需要将一些照片拼接在一起，首先想到了使用APP直接操作，结果下载了许多应用后发现最多只能支持九张照片的拼接。然后又找了些美图秀秀之类，都无法满足我的需求，甚至我都想到使用PS去进行操作，但是如果使用PS那可就变成了一项耗时间的活了呢。于是继续的查找解决方案，在一个小角落里找到了使用Pillow搭建照片墙的例子，心想这就是我想要的，细细查找发现果不其然，一下子明朗了许多。在此对使用Python + Pillow完成的拼图实现进行记录。



<!--more-->

## 安装Python与Pillow

可参考之前的博文，[Python及其库的安装](http://www.airbird.info/2018/sw-python-install/)。



## 流程及思路

**需求**：将一个文件夹中按名称排序的方式进行拼图操作，逐行或逐列操作。

**预计流程**：

* 创建临时文件夹缓存可能生成或后续需要使用的图片
* 读取图片，进行预处理后将处理后图片按照一定命名规范保存至缓存文件夹
* 切换路径至临时文件夹
* 依次打开图片，进行图像合并
* 合并完成后保存图片
* 删除临时文件夹
* 展示合并图片



其中图片预处理可以为拉伸、旋转、裁剪等变换，因为我后续需要拼图时所有照片都应该为正方形，因此我需要对图片进行一个裁剪操作使图片比例为1:1，为了保证裁剪区域在图像正中，需要进行判断长短边操作。

进行合并图片时需要空余区域尽可能少，且合并图片比例不能太畸形。例如30张图片可以分为5×6排布，31张照片可以分布为4×8排布。最理想状态是脚本自动识别图片个数并合理分配，这块功能暂时没有写入DEMO中，行与列目前需要手动分配。

## DEMO

在Python脚本中引用Pillow的方法也可以参见DEMO程序。其中，

`bol_auto_place`暂时为可选项，置为`True`表示将自动分配合并后画布大小，目前只有根据图片多少开平方，然后合并为一个大正方形图片，手动设置合并排布时需要将其置为`False`。

`row`为合并图片分布行参数，`bol_auto_place == False`时有效。

`col`为合并图片分布列参数，`bol_auto_place == False`时有效。

`nw`为缓存图片宽度设定，`nh`为缓存图片高度设定。合并文件的大小由排布及缓存图片大小自动设定。



DEMO脚本中所使用到的一些function有不懂的可百度或谷歌，查看各自的详细描述。脚本在使用时与图片放在一起，然后点击运行，运行期间将会显示当前处理图片，处理完成后将会展示合并图片。合并完成后图片以PNG格式存储于同路径下`splicing_picture.png`文件。DEMO程序的源代码及几个参考文件可[点此进行下载](http://o85gvbiad.bkt.clouddn.com/20180503-sw-python-pillow-pintu.zip)。

```python
#####################################################
# Notice !                                          #
# This script file should be placed in the same     #
# folder as the image.                              #
#####################################################

import sys, os, shutil, math
from PIL import Image

#####################################################
# parameter setting                                 #
#####################################################
bol_auto_place = False                     # auto place the image as a squared image， if 'True', ignore var 'row' and 'col' below
row            = 4                         # row number which means col number images per row
col            = 8                         # col number which means row number images per col
nw             = 400                       # sub image size, nw x nh
nh             = 400

path = os.getcwd();          # acquire current folder path

if os.path.exists('tmp'):    # ensure the 'tmp' folder is empty
   shutil.rmtree('tmp')
os.makedirs('tmp')

file_ls = os.listdir()       # list all files in this folder

i = 0                        # a counter for images
for file in file_ls:
	name, extension = os.path.splitext(file);    # get file info[name, extension]
	if (extension == '.png' or extension == '.jpg' or extension == '.jpeg') and name != 'splicing_picture':    # select the image
		i += 1                               # image counter++
		print('%s...%s%s' % (i, name, extension))
		os.chdir(path)                       # ensure the image folder in every loop
		im = Image.open(file)                # open the image
		w, h = im.size                       # get image info
		#print('Original image size: %sx%s' % (w, h))
		if nw == nh:                         # if image should be 1:1 size
			if w >= h:
				box = ((w - h) // 2, 0, (w + h) // 2, h)
			else:
				box = (0, (h - w) // 2, w, (h + w) // 2)
			region = im.crop(box)            # crop the image to 1:1 and keep center region
		else:
			region = im                      # do nothing
		sname = '%s%s' % (str(i), '.png')    # rename 'x.png', x is a number from 1 to N
		os.chdir('tmp')                      # get into the folder 'tmp'
		region.save(sname, 'png')            # save the square image

os.chdir(path)        # ensure the path
os.chdir('tmp')

if bol_auto_place:    # auto place a big 1:1 square image 
	row = math.ceil(i ** 0.5)
	col = math.ceil(i ** 0.5)

dest_im = Image.new('RGBA', (col * nw, row * nh), (255, 255, 255))    # the image size of splicing image, background color is white

for x in range(1, col + 1):          # loop place the sub image
	for y in range(1,row + 1):
		try:
			src_im = Image.open("%s.png" % str( x + ( y - 1 ) * col))  # open files in order
			resize_im = src_im.resize((nw, nh), Image.ANTIALIAS)       # resize again
			dest_im.paste(resize_im, ((x-1) * nw, (y-1) * nh))         # paste to dest_im
		except IOError:
			pass

os.chdir(path)        # ensure the path
shutil.rmtree('tmp')  # delete the 'tmp'

dest_im.save('splicing_picture.png', 'png')
dest_im.show()        # finish

```

## 运行效果图

30张照片按照4×8的排布方式，图片拼合后效果图如下所示。个人对这样的结果还是相当满意的，也可以调整成5×6的排布方式，只需更改`row`与`col`的参数设定后重新运行即可。

![30张照片拼图](http://o85gvbiad.bkt.clouddn.com/20180503-sw-python-pillow-pintu.png)