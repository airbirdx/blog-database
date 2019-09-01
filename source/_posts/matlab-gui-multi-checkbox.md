---
title: 原创 | Matlab 之复选框使用
date: 2016-12-22 20:43:10
categories:
  - Matlab
tags:
  - Matlab
---

本文简单记录在 Matlab 的 GUI 设计中，复选框的一些使用，比较简单。

<!--more-->

简单到直接上代码，就是可能比较容易忘记，使用的时候再翻回来好了。

```matlab
% 复选框，选中后为 1，未选中则为 0
function chechbox_Callback(hObject, eventdata, handles)
if ( get(hObject,'Value') )
    SW_Checkbox = 1;
else
    SW_Checkbox= 0;
end
```

另外有关于其初值，可以使用全局变量进行设置（已经个人验证），好像也可以直接修改其属性进行修改（未验证）。