#! /usr/bin/env python
# coding=utf-8

# 使用python xmlrpc 发送内容到博客园
# https://rpc.cnblogs.com/metaweblog/airbird 从链接可以看到支持的metaweblog API
import xmlrpc.client as xmlrpclib
import glob
import os
import sys
import json
import time
import datetime
import ssl
import re
import shutil
import subprocess
ssl._create_default_https_context = ssl._create_unverified_context


pst_path = "./cnblog_posts/"       # 发布文章路径(article path)
art_path = "./rename_posts/"
cfg_file = "cnblog_config.json"    # 博客配置路径(config path)
recentnum = 99999                  # 获取文章篇数

url = appkey = blogid = usr = passwd = ""
server = None
mwb = None
title2id = {}

# -----配置读写操作-----
'''
配置字典：
type | description(example)
str  | metaWeblog url, 博客设置中有('https://rpc.cnblogs.com/metaweblog/nickchen121')
str  | appkey, Blog地址名('nickchen121')
str  | blogid, 这个无需手动输入，通过getUsersBlogs得到
str  | usr, 登录用户名
str  | passwd, 登录密码
'''


def mkdir(path):
    '''
    防止目录存在
    '''
    if not os.path.exists(path):
        os.mkdir(path)


def rmdir(path):
    '''
    删除整个目录
    '''
    if os.path.exists(path):
        shutil.rmtree(path)
        
        
def exist_cfg():
    '''
    返回配置是否存在
    '''
    try:
        with open(cfg_file, "r", encoding="utf-8") as f:
            try:
                cfg = json.load(f)
                if cfg == {}:
                    return False
                else:
                    return True
            except json.decoder.JSONDecodeError:  # 文件为空
                return False
    except:
        with open(cfg_file, "w", encoding="utf-8") as f:
            json.dump({}, f)
            return False


def create_cfg():
    '''
    创建配置
    '''
    while True:
        cfg = {}
        for item in [("url", "metaWeblog url, 博客设置中有\
            ('https://rpc.cnblogs.com/metaweblog/blogaddress')"),
                     ("appkey", "Blog地址名('blogaddress')"),
                     ("usr", "登录用户名"),
                     ("passwd", "登录密码")]:
            cfg[item[0]] = input("输入 " + item[1] + ' :')
        try:
            server = xmlrpclib.ServerProxy(cfg["url"])
            userInfo = server.blogger.getUsersBlogs(
                cfg["appkey"], cfg["usr"], cfg["passwd"])
            print(userInfo[0])
            # {'blogid': 'xxx', 'url': 'xxx', 'blogName': 'xxx'}
            cfg["blogid"] = userInfo[0]["blogid"]
            break
        except:
            print("发生错误！")
    with open(cfg_file, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=4, ensure_ascii=False)


def get_cfg():
    '''
    获取当前文章列表
    '''
    global url, appkey, blogid, usr, passwd, server, mwb, title2id
    with open(cfg_file, "r", encoding="utf-8") as f:
        cfg = json.load(f)
        url = cfg["url"]
        appkey = cfg["appkey"]
        blogid = cfg["blogid"]
        usr = cfg["usr"]
        passwd = cfg["passwd"]
        server = xmlrpclib.ServerProxy(cfg["url"])
        mwb = server.metaWeblog
        # title2id[title]=postid  储存博客中文章标题对应的postid
        print(cfg["blogid"], cfg["usr"], recentnum)
        recentPost = mwb.getRecentPosts(
            cfg["blogid"], cfg["usr"], cfg["passwd"], recentnum)
        for post in recentPost:
            # 1.把datetime转成字符串
            dt = post["dateCreated"]
            # post["dateCreated"] = dt.strftime("%Y%m%dT%H:%M:%S")
            post["dateCreated"] = dt.__str__()
            # 2.把字符串转成datetime
            # datetime.datetime.strptime(st, "%Y%m%dT%H:%M:%S")
            # datetime.datetime.fromisoformat(str)
            title2id[post["title"]] = post["postid"]


def newPost(blogid, usr, passwd, post, publish):
    while True:
        try:
            postid = mwb.newPost(blogid, usr, passwd, post, publish)
            break
        except:
            time.sleep(5)
    return postid


def post_art(path, publish=True):
    # print(path)
    title = os.path.basename(path)  # 获取文件名做博客文章标题
    # print(title)
    [title, _] = os.path.splitext(title)  # 去除扩展名
    with open(path, "r", encoding="utf-8") as f:
        post = dict(description=f.read(), title=title)
        # post["categories"] = ["[Markdown]"]
        # mt_keywords
        # print(title)
        if title in title2id.keys():  # 博客里已经存在这篇文章
            mwb.editPost(title2id[title], usr, passwd, post, publish)
            print(title)
            print("Update:[title=%s][postid=%s][publish=%r]" %
                  (title, title2id[title], publish))
            return (title, title2id[title], publish)

        else:  # 博客里还不存在这篇文章
            postid = newPost(blogid, usr, passwd, post, publish)
            print("New:[title=%s][postid=%s][publish=%r]" %
                  (title, postid, publish))
            return (title, postid, publish)


def download_art():
    '''
    下载文章
    '''

    # 获取最近文章，并获取所有文章信息
    recentPost = mwb.getRecentPosts(blogid, usr, passwd, recentnum)
    for post in recentPost:
        with open(art_path + post["title"] + ".md",
                  "w", encoding="utf-8") as f:
            f.write(post["description"])


def cnblog_initial():
    # 创建用户配置
    if not exist_cfg():
        create_cfg()

    # 获取文章参数
    get_cfg()


def cnblog_post():
    '''
    发布文章
    '''
    for mdfile in glob.glob(art_path + "*.md"):
        print(mdfile)
        post_art(mdfile, True)

def hexo2cnblog():
    for mdfile in glob.glob(pst_path + "*.md"):
        # print(mdfile)
        # exit()

        f = open(mdfile, "r", encoding="utf-8")
        mdcontents = f.read()
        f.close()

        header = re.compile('(?<=---)[\s\S]+?(?=---)').search(mdcontents)
        if header:
            header = header.group(0)
        else:
            print('header error, exit...')
            exit()

        flag_title      = re.compile('(?<=title:).*').search(header)
        flag_date       = re.compile('(?<=date:).*').search(header)
        flag_categories = re.compile('(?<=categories:)[\s\S]+(?=tags)').search(header)
        flag_tags       = re.compile('(?<=tags:)[\s\S]+$').search(header)

        cnblog_title = ''
        categories = []
        tags = []

        if flag_title:
            hexo_title = flag_title.group(0)
            # print(hexo_title)
            type = re.compile('^[\s\S]+(?=\|)').search(hexo_title).group(0).strip()
            title = re.compile('(?<=\|)[\s\S]+$').search(hexo_title).group(0).strip()
            cnblog_title = '[' + type + ']' + title

        if flag_categories:
            for tmp in flag_categories.group(0).split('\n'):
                if '- ' in tmp.strip():
                    categories.append(tmp.strip()[2:])

        if flag_tags:
            for tmp in flag_tags.group(0).split('\n'):
                if '- ' in tmp.strip():
                    tags.append(tmp.strip()[2:])

        contents = mdcontents.replace(header, '').strip()
        contents = contents.replace('------', '').strip()

        # cnblog_title, categories, tags
        
        f = open(art_path + cnblog_title + '.md', "w", encoding="utf-8")
        f.write(contents)
        f.close()


def get_update_blogs():
    blogs = []
    p = subprocess.Popen('git status', shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while p.poll() is None:
        line = p.stdout.readline()
        line = line.strip().decode('utf-8') 
        # print(type(line))
        if line:
            if 'modified:' in line and 'source/_posts' in line and '.md' in line:
                blogs.append(line)
            # print('Subprogram output: [{}]'.format(line))
    # if p.returncode == 0:
    #     print('Subprogram success')
    # else:
    #     print('Subprogram failed')
    # print(blogs)
    res = []
    for tmp in blogs:
        mdfile = tmp.split('/')[-1]
        # print(mdfile)
        shutil.copy('./source/_posts/' + mdfile, pst_path)
    

def auto_cnblog():
    mkdir(pst_path)
    mkdir(art_path)
    
    get_update_blogs()

    hexo2cnblog()

    cnblog_initial()
    cnblog_post()
    
    rmdir(pst_path)
    rmdir(art_path)

if __name__ == "__main__":
    # auto_cnblog()
    pass
    

