#!/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author : OnePointTwo
# @File : dataclean.py
# @Time : 2020/3/29 22:35
# @Desc ：正则清理文本数据

import pandas as pd
import re

inputpath = './data/input.xlsx'
outputpath  = './output/output.csv'

def read_file(path):
    data = pd.read_csv(path,encoding='utf-8')
    return data

def dataclean(str):
    str_doc = ''
    # 1.正则过滤特殊符号、标点、英文、数字等
    re1 = '[a-zA-Z0-9]！"#$%&\'()*~＆&“”‘’〝〞()+-./:：;；|<=>?@，-。？…、!～.]^_{|}~]+'

    # 2. 去除空格
    re2 = '\s+'
    str_doc = re.sub(re1,' ',str_doc)
    str_doc = re.sub(re2, ' ', str_doc)

    # 3. 去除换行符
    #str_doc = str_doc.replace('\n','')

    return str_doc

if __name__ == '__main__':
    # 1.读取文本数据
    inputdata = read_file(inputpath)
    data = dataclean(inputdata)
    data.to_csv(outputpath, index=False, encoding='UTF-8', na_rep='')




