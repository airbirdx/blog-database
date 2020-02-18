import sys
import os
import re
import datetime

def md_lst(path):
    res = []
    file_lst = os.listdir(path)  # list all files in this folder
    file_lst.sort()
    for file in file_lst:
        name, ext = os.path.splitext(file)
        if ext == '.md':
            res.append(file)
    return res


def get_info_from_mdfile(mdfile):
    f = open(mdfile, 'r', encoding='utf-8')
    mdcontexts = f.read()
    f.close()

    header = re.compile('(?<=---)[\s\S]+?(?=---)').search(mdcontexts)
    if header:
        header = header.group(0)
    else:
        print('header error, exit...')
        exit()

    flag_title      = re.compile('(?<=title:).*').search(header)
    flag_date       = re.compile('(?<=date:).*').search(header)
    flag_categories = re.compile('(?<=categories:)[\s\S]+(?=tags)').search(header)
    flag_tags       = re.compile('(?<=tags:)[\s\S]+$').search(header)

    # print(flag_title)
    # print(flag_date)
    # print(flag_categories)
    # print(flag_tags)

    if flag_title:
        res_title = 'NULL'
        tmp = flag_title.group(0)
        res_title = tmp.strip()

    if flag_date:
        res_year = 'NULL'
        # tmp = flag_date.group(0).split('-')
        tmp = flag_date.group(0).strip()
        res_date = tmp

    if flag_categories:
        res_categories = []
        for tmp in flag_categories.group(0).split('\n'):
            if '- ' in tmp.strip():
                res_categories.append(tmp.strip()[2:])
        if res_categories == []:
            res_categories = ['NULL']

    if flag_tags:
        res_tags = []
        for tmp in flag_tags.group(0).split('\n'):
            if '- ' in tmp.strip():
                res_tags.append(tmp.strip()[2:])
        if res_tags == []:
            res_tags = ['NULL']
    
    if mdfile:
        tmp = mdfile.split('/')
        res_link = tmp[-1][:-3]

    res = [res_title, res_date, res_link, res_categories, res_tags]
    # print(res)
    # exit()
    return res


def gen_toc_mdfile(mdfile, toc_info):
    contexts = []
    contexts.append('---')
    contexts.append('title: 目录 | 置顶汇总')
    contexts.append('date: %s' % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    contexts.append('categories:')
    contexts.append('  - TOC')
    contexts.append('tags:')
    contexts.append('  - TOC')
    contexts.append('---')

    tmp = []
    for item in toc_info:
        tmp += item[3]
    all_cate = list(set(tmp))
    all_cate.sort()

    re_info = []
    for tmp in toc_info:
        title, date, link, categories, tags = tmp        
        p_title = title
        p_link = 'www.airbird.info/' + date[:4] + '/' + link
        for p_cate in categories:
            re_info.append([p_cate, p_title, p_link, date])

    for cate in all_cate:
        cate_info = []
        for tmp in re_info:
            if cate == tmp[0]:
                cate_info.append(tmp)
        cate_info2 = sort_by_col(cate_info, 3)

        contexts.append('')
        contexts.append('## %s' % cate)
        for item in cate_info2:
            title, link, date= item[1:]
            contexts.append('* %s ->> [%s](%s)' % (date[:10], title, link))
    
    f = open(mdfile, 'w', encoding='utf-8')
    for line in contexts:
        f.writelines(line + '\n')
    f.close()


def sort_by_col(lst, col):
    i0 = lst[0]
    if col >= len(i0) or type(i0) != type([]):
        print('error')
        exit()

    sel = []
    for tmp in lst:
        sel.append(tmp[col])
    sel.sort(reverse=True)
    
    index = []
    for i in range(len(sel)):
        for j in range(len(lst)):
            if sel[i] == lst[j][col]:
                if j not in index:
                    index.append(j)
                    break
    
    res = []
    for i in index:
        res.append(lst[i])

    return res


def gen_toc():
    script_path = sys.path[0]
    src_path = script_path + '/source/_posts'
    toc_info = []
    for mdfile in md_lst(src_path):
        if mdfile != 'blog-toc.md':
            tmp = get_info_from_mdfile(src_path + '/' + mdfile)
            toc_info.append(tmp)
    gen_toc_mdfile(src_path + '/blog-toc.md', toc_info)


if __name__ == '__main__':
    main()
