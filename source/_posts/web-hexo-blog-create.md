---
title: 原创 | HEXO 博客搭建日记
date: 2016-11-10 10:42:28
categories:
  - Web
tags:
  - HEXO
---

博客系统折腾了好久，使用过 Wordpress，Ghost，Typecho，其中 Typecho 是我使用起来最舒心的一种，Markdown 编辑 + 轻量化设计，功能不多不少刚好，着实让我这种强迫症患者舒服了好久。但是有那么一天，我的主机空间和 Typecho 突然冲突了，求助了好久也没有得到解决办法，最终不得已开始考虑更换，因为在 Typecho 上使用的就是移植的 NexT 主题，于是就对 HEXO 有了些兴趣，再加上 HEXO 也是原生的 Markdown 编辑，最终思量再三后决定就是 HEXO 了。

下面是我参考了网上的一些博文的安装教程后对自己安装的一个记录，希望可以帮助到对HEXO有兴趣的人。

> 2018.04.10 更新：修改章节顺序使得文章条理更清楚
>
> 2017.02.09 更新：添加将 HEXO 部署到 Coding 上的内容
>
> 2017.06.25 更新：更改部分小错误，并添加 hexo sever失常的一种情况及解决方案

<!--more-->

## HEXO介绍

HEXO 是一个快速、简洁且高效的博客框架。可以方便快捷的生成博客网页。HEXO 是一个基于 Node.js 的静态博客程序，可以支持多种主题。总之，HEXO 加上 GitHub Pages 就可以搭建一个免费的博客空间了，而且访问速度也还是可以的哦。

由于在国内，上 GitHub 的速度不是特别让人满意，同时 Coding 也有了静态网页的服务推出，于是就想到了同时托管到两个平台的想法，这样国内线路可以使用 Coding，国外线路使用 GitHub，加快网页打开速度。查阅了相关资料后对本文进行了详细的补充。同时还有人将 HEXO 部署到腾讯云上，也是很不错的选择。

好了闲话不再多说，让我们进入今天的主题，基于 HEXO + Pages 服务的博客搭建。

## Node.js安装

在上面的介绍中我们也都知道了 HEXO 是基于 Node.js 的博客框架，那么作为主体的 Node.js 是必不可少的了，有关其下载，可以进入 [Node.js 官网](https://nodejs.org/en/)或者 [Node.js 中文网](http://nodejs.cn/)进行下载。

下载完成后可以运行然后一路确认安装（即按照默认配置），其中安装路径可以根据自己喜好进行修改，安装完成后可以使用快捷键 win + R 打开 cmd 命令行，在其中可以输入以下命令行进行 Node 版本信息的查看，如果可以正常观察到版本信息，则说明 Node.js安装成功，此部分就告一段落，否则需要重装 Node.js。
```
node -v	# 查看node版本号
npm -v	# 查看npm版本号
```
## Git安装

Git软件是一个分布式版本控制工具，但是我们在此仅仅用到了一点点的功能，一些关于 Git 的详细介绍可以点此进行查阅。Git 软件的下载可以在[官网](https://git-scm.com/)，如果觉得下载速度慢也可以在国内热心人搭建的[下载站](https://GitHub.com/waylau/git-for-win)进行下载，国内下载站版本可能稍有落后。

有人选择在软件安装中如下界面处将选项设置为 **Use Git from Windows CMD prompt**，这里主要是为了在 windows 的 CMD 下对 Git 进行些设置（因为默认是只能在 Git Bash 中执行的）。但是仍然有些操作只能在 Git Bash 下运行，但是选择这个确实更加方便一些。其他地方一路默认即可（同上，安装路径自定义）。

![Git安装](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20160607-hexo-blog-created-git-setup.png)

在按照上述的安装后我们一样打开 CMD 来运行一条指令来看下 Git 的版本号。
```
git --version	  # 查看 Git 版本号
```
如果正常显示，则安装成功，继续后面步骤，反之需要重新安装。

## HEXO安装

在命令行中输入以下命令进行 HEXO 的安装
```
npm install -g hexo	# 安装 HEXO
```

可能会出现一个 WARNING，但是没有很大关系，继续下面操作即可。

~~npm install hexo --save	# 保存 HEXO~~

此时我们可以使用如下命令来看所安装HEXO的版本号

```
hexo -v	# 查看 HEXO 版本号
```

本人的版本显示结果可参考如下

```
hexo: 3.2.2
hexo-cli: 1.0.2
os: Windows_NT 10.0.14393 win32 x64
http_parser: 2.7.0
node: 6.9.5
v8: 5.1.281.89
uv: 1.9.1
zlib: 1.2.8
ares: 1.10.1-DEV
icu: 57.1
modules: 48
openssl: 1.0.2k
```

## HEXO初始化

在硬盘上选择一个合适的位置，新建一个空文件夹（最好为英文路径）作为存放博客数据的地方。使用 `Shift+鼠标右键(Windows 系统)` 的方式打开命令行，这样路径就自动设置在当前路径下了，后续若有打开命令行操作，还都以此方式打开。

然后我们继续进行 HEXO 博客初始化的操作，在命令行中继续键入
```
hexo init	# 初始化组件
```
进行博客的初始化搭建。上述命令执行完就可以看到文件路径下有了一些文件，这些都是你博客运行所需要的文件。


使用
```
hexo g	# 生成 public 静态文件
```
生成静态页面，然后使用
```
hexo s	# 启动服务器，查看本地效果
```
启动本地服务，进入文章预览调试。在[http://localhost:4000](http://localhost:4000)下就可以看到所生成的静态页面了

也可以使用
```
hexo s --debug
```
来查看调试的详细模式，会有每个改动信息提示。

![HEXO初始界面](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20160607-hexo-blog-created-localhost.png)

***可能的错误及解决办法***：本部分参考了文章[localhost:4000不能访问](http://blog.csdn.net/u012246342/article/details/51543370)。

在第二次搭建HEXO时，在 `hexo sever` 的时候没能正常打开调试模式下的网页，经过一些列查明，发现 4000 端口被占用了（查询命令`netstat -an|findstr 4000`），那么退而求其次，我们可以更换一个端口来运行 HEXO 的调试模式，命令改为
```
hexo s -p 5000	# 启动服务器，查看本地效果，端口号 5000
```
就可以在 [http://localhost:5000](http://localhost:5000) 下进行阅览。


## Pages配置

### GitHub

这里需要一个 GitHub 账号，没有的请进入 [GitHub 官网](https://GitHub.com/)自行申请，这里不多描述申请。在有了一个账号之后，进行网站代码库的部署。首先新建一个知识库，在右上角找到` + 号`，然后选择 **New repository**，进入代码库创建页面,如下图。

![New repository](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20160607-hexo-blog-created-github.png)

在 **Repository name** 那里填写 **yourname.GitHub.io**。注意此处的 **yourname** 为你的GitHub账户名，格式必须按照上文中所说的来。**Description** 部分选填，空间类型选择 **Public** ，然后点击 **Create repository** 进行创建，创建完成后将会看到这样的一个空间。

![Repository](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20160607-hexo-blog-created-github-new.png)

然后我们点击界面中的 Setting，就是那个小齿轮，向下拖动，看到 **GitHub Pages** 部分，点击 **Automatic page generator**，然后一路向下，系统会自行的给你创建一个网页，稍微等待一会儿，就可以发现 **yourname.GitHub.io** 这个网址已经可以打开了。

后续帮同学设置时发现 **Auto** 的选项消失了，如下图

![Choose a theme](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20180416-hexo-blog-created-github-gpages-info.png)

点击 **Choose a theme**，进入选择页面，然后点击 **Select theme**，在新的页面再点击 **Commit Change** 自动提交至 GitHub Repository 就完成了 **GitHub Pages** 的创建了。至此，GitHub 网站部署完成。

### Coding

和上述 GitHub 部署的方法类似，首先是申请一个 Coding 的账户，申请邮箱最好一致，这样就可以共用后面我们要说到的 SSH Key 了。

之后在 Coding 上创建一个项目，**项目名称最好与你的账户名称一致**，这样后续操作起来会比较方便，不容易发晕与出错。

![New Project](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20170209-coding-new-project.png)

和 GitHub 有些不同，Coding 的 Pages 服务我们等后续Git部署完成了后再进行，在完成以上的创建后我们留先进入下一个阶段。

Coding 的部署方式有两种，第一种就是 pages 服务的方式，也就是和 GitHub 一样，也是我们推荐的方式，其可以绑定域名；第二种演示方式必须升级会员才能绑定自定义域名。

Coding 使用 Pages 服务时需要在本地创建一个空白文件 `Staticfile`，coding.net 需要使用这个文件来作为静态文件部署的标志。即看到这个叫做 `Staticfile` 的空白文件就知道按照静态网页来进行发布，在 hexo 所在文件夹下键入。

```
cd source/	      #进入 source 文件夹
touch Staticfile  #名字必须是 Staticfile
```

然后在 Coding 中进入你刚才所创建的项目，点击`代码 -->> Pages 服务`，将其启用，部署来源选择选择 Master 分支（默认，不用更改）。

## Git部署

### 生成SSH Key

在 GitHub 部署完成后，需要对电脑客户端的Git进行配置部署。此步骤主要是添加 SSH-Key。首先使用你的 GitHub 用户名和密码进行配置，在空白处鼠标右键选择 **Git Bash Here** 进入 Git 命令行，键入以下两条指令。
```
git config --global user.name "yourname"
git config --global user.email "web@webmail.com"
```
其中，**web@webmail.com** 为你申请GitHub账户时使用的邮箱，**yourname** 为 GitHub 的用户名。

之后，生成密钥。
```
ssh-keygen -t rsa -C "web@webmail.com"
```
然后一路默认回车，最后它将会生在**默认路径**生成一个`.ssh`的文件夹（注意改文件夹路径），里面会有一个 **id_rsa** 和 **id_rsa.pub** 的文件。这是我使用命令行生成后的结果，不同用户所产生的名字可能略微有不同。这里确保自己的密钥文件不要在电脑上剪切或删除，后续Git部署时找不到密钥会提示警告且部署失败。

### 网站添加SSH Key

使用编辑器打开 **id_rsa.pub** 文件，复制其中的内容。

1. \[GitHub\]打开 GitHub 的 Setting -->> SSH and GPG keys，添加到自己的 SSH Key。若找不到位置，可以[点此快速进入](http://GitHub.com/settings/ssh)。
2. \[Coding\]打开 Coding 的账户 -->> SSH公钥，添加自己的 SSH Key。若找不到位置，可以[点此快速进入](https://coding.net/user/account/setting/keys)。

### 本地Git配置

~~将上面生成的.ssh文件夹复制到Git的安装路径，比如我的就是`D:\Program Files\Git\.ssh`。**（不复制也可以，只要后续使用命令验证，故此步骤多余）**~~

然后可以可以使用如下命令验证一下，期间可能需要自己进行 yes 选项的确定，正常操作后就会出现成功连接的提示。若无则重新进行 Git 部署部分的操作。
1. \[GitHub\]
```
ssh -T git@GitHub.com
```
2. \[Coding\]
```
ssh -T git@git.coding.net
```

这两部分的验证，我所得到的提示如下可以参考（可能略有出入，但大概都是这个意思）。
1. \[GitHub\]（其中xxx为用户名）
```
Hi xxx! You've successfully authenticated, but GitHub does not provide shell access.
```
2. \[Coding\]（其中xxx为用户名）
```
Hello xxx! You've connected to Coding.net via SSH successfully!
```

## HEXO + Git部署

### 配置修改

首先在命令行中键入
```
npm install hexo-deployer-git --save		# 安装使用 git 方式进行部署所需要的插件
```
来进行 git 同步上传时所需要的插件。

在我们所设定的路径下，安装HEXO后生成了一些文件，其中 **_config.yml** 文件需要重点说一下，这个文件可以说是我们的 **站点配置文件**，里面有着网站的一些信息。在建立与 GitHub 的关联时，我们需要编辑这个文件，使用编辑器打开 **_config.yml** 文件，翻到最下面的 **deploy** 配置项，改成如下的样式（其中 yourname 为在两个平台的用户名）。
```
deploy:
  type: git
  repo:
    coding: git@git.coding.net:airbird/yourname.git
    GitHub: git@GitHub.com:CNairbird/yourname.GitHub.io.git
  branch: master
```
我看有些博文中也有在 repo 项直接使用url形式的，类似这种
```
https://GitHub.com/yourname/yourname.GitHub.io.git
```
但是我在搭建过程中这种写法却遇到了一些问题，未能成功，**建议还是使用上面提到的第一种方法**。更改完成后保存关闭文件，

### 网站部署

之后在命令行中键入部署命令将 HEXO 博客的内容部署到网站上。
```
hexo d	# 部署（部署到 Coding 与 GitHub 上）
```
执行完成后，（1）Github 上的就可以在浏览器中键入 yourname.github.io 进行博客的打开了；（2）Coding 上网址一般为 yourname.coding.me。

**其中：**如果你的项目名称跟你 coding 的用户名一样，比如我的用户是叫 airbird ,博客项目名也叫 `airbird` .那直接访问 `airbird.coding.me` 就能访问博客，否则就要带上项目名 `airbird.coding.me/项目名` 才能访问。因此我们前面才会**推荐项目名跟用户名一样**，这样就可以省略项目名了

到这里，HEXO + Git 的部署以及博客的基本搭建就完成了。

## 域名解析

如果你入手了一个域名，想要将域名解析到你的 HEXO + GitHub 博客地址，那要怎么做呢？

### 设置CNAME

在博客目录下的 `source` 文件夹下，创建一个 `CNAME` 的文件，里面内容设定为你的域名，我的就是
```
www.airbird.info
```
### 域名解析

在你的域名解析商处添加解析信息，添加这样的两条解析内容。只需要将你的记录值按照你自己的更改为 **yourname.github.io** 和 **yourname.coding.me** 即可。

![域名解析](https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/20170209-dnspod-new-setting.png)

这里我使用的解析服务是 DNSPod，这里因人而异，你的可能是域名购买商本身的解析服务也可能是别的地方的解析服务，不过更改的办法都是大同小异。解析更改到开始运行都有着一定的等待刷新时间，还请耐心等待。不过我使用 DNSPod 来看，还是很快的，不一会就可以通过自有域名进入到你的博客了。

注意这里国内使用 Coding，国外使用 GitHub 哦。

## 书写一篇博文

在 HEXO 框架下，书写博文首先需要在命令行中键入
```
hexo new "postname"
```
它会在博客文件下 source/_posts 路径下生成一个 “postname.md” 的 Markdown 文档供你保存。

当然你也可以将编辑完成的md文件直接复制进来，它一样会显示在网站上。注意，这里在网站上的显示顺序是按照文档的第一次部署时间排序后进行显示的。

**这里的md文档和一般的md文档还有些微的差别**，比如在文章的开头需要有着标题、分类、标签这些消息。类似下面的这种。
```
---
title: post title（这里是文章显示的标题）
categories:
  - cate（文章的分类）
tags:
  - tag1（文章标签）
  - tag2（文章标签）
---

博文内容...
```
在每次添加内容后，最好都在命令行中使用以下3个命令来保证页面信息的同步。
```
hexo clean	# 清除之前 public 文件夹的内容
hexo g		  # 生成静态的 public 文件夹，部署时候也是直接拷贝此文件夹里的文件。
hexo d		  # 部署到 GitHub 上
```
部署完成后就可以刷新页面进行查阅了。

## HEXO常用命令

### 单条指令
```
hexo new "postName" 		  # 新建文章
hexo new page "pageName" 	# 新建页面
hexo clean  			        # 清除之前 public 文件夹的内容
hexo generate 			      # 生成静态页面至 public 目录
hexo deploy 			        # 将 .deploy 目录部署到 GitHub
hexo server 			        # 开启预览访问端口（默认端口 4000，'ctrl + c'关闭 server）
hexo help  			          # 查看帮助
hexo version  			      # 查看 HEXO 的版本
```
### 简写指令
```
hexo n == hexo new
hexo g == hexo generate
hexo d == hexo deploy
hexo s == hexo server
hexo v == hexo version
```
### 复合指令
```
hexo deploy -g           #生成加部署
hexo server -g           #生成加预览
hexo d --g / hexo g --d	 #生成加部署
```

## 参考感谢

[1] [hexo你的博客](http://ibruce.info/2013/11/22/hexo-your-blog/)
[2] [史上最详细的Hexo博客搭建图文教程](https://xuanwo.org/2015/03/26/hexo-intor/)
[3] [Hexo + Git 搭建免费的个人博客](http://www.cylong.com/blog/2016/04/19/hexo-git/)
[4] [HEXO+GitHub,搭建属于自己的博客](http://www.jianshu.com/p/465830080ea9)
[5] [Hexo搭建GitHub静态博客](http://www.cnblogs.com/zhcncn/p/4097881.html)
[6] [Hexo博客同时部署至GitHub和Coding](http://blog.csdn.net/u011303443/article/details/51509351)