---
title: 原创 | Matlab 自动复制文件夹中图片
date: 2018-05-03 16:41:30
categories:
  - Matlab
tags:
  - Matlab
---

进行性能评估后生成了很多图片，在使用Latex进行报告的编写时，发现照片都要一个个从一个文件夹粘贴到对应的文件夹中，而文件夹又有很多，手动一个一个文件夹的粘贴太麻烦了，正巧之前是使用 Matlab 进行的数据处理，于是简单写了个程序进行文件夹及其中图片的自动复制。

所实现功能比较简单，如有后续需求可自行根据DEMO进行延拓。

<!--more-->

## DEMO

功能比较简单，有 matlab 语法基础的配合注释基本都能看懂了，使用到的一些 function 如果有不懂的或者想要了解的，可以直接在 matlab 程序中 help 或者 doc 查看用法。

DEMO中仅描述了复制后缀为 '.png' 的文件，如果有别的需要，可以根据相应后缀以及逻辑符进行更改。

```matlab
clc; clear; close all; warning off all;

src_path    = 'xx';                                                         % 源路径
dest_path   = 'xx';                                                         % 目的路径

cd  (src_path);                                                             % 切换至源路径
dir_src = dir;                                                              % 获取路径下所有项目    

for i = 1:length(dir_src)                                                   % 循环处理路径下所有子项目
    if dir_src(i).isdir                                                     % 判断是否为文件夹路径
        name_str = dir_src(i).name;                                         % 获取名称
        if strcmp(name_str, '.') || strcmp(name_str, '..')                  % 跳过'.'和'..'两个路径
            continue;
        end
        
        cd  (dest_path);                                                    % 切换到目的路径
        if ~exist(name_str, 'dir')                                          % 如果没有同名文件夹，创建
            mkdir(name_str);
        end

        cd ([src_path '\' name_str]);                                       % 返回源路径并进入子路径
        file_in_folder = dir;                                               % 获取当前子路径下所有项目
        for n = 1:length(file_in_folder)                                    % 循环处理
            file_name = file_in_folder(n).name;                             % 获取名称
            if strfind(file_name, '.png')                                   % 选择后缀为'.png'的项目
                copyfile(file_name, [dest_path '\' name_str], 'f');         % 将其复制至目的文件夹，'f'表示force
            end
        end
    end
end
```

