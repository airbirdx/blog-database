import os

old_link = 'http://o85gvbiad.bkt.clouddn.com/'
new_link = 'https://airbird-1252162485.cos.ap-shanghai.myqcloud.com/'

post_path = './source/_posts/'

lst = os.listdir(post_path)  # list all files in this folder
lst.sort()

for file in lst:
    name, ext = os.path.splitext(file)
    if ext == '.md':
        f = open(post_path + file, 'r', encoding='utf-8')
        txt = f.read()
        f.close()

        new_txt = txt.replace(old_link, new_link)
        
        f = open(post_path + file, 'w', encoding='utf-8')
        f.write(new_txt)
        f.close()

