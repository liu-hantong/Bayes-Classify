#! python3
# -*- coding: utf-8 -*-
# Create by Hantong Liu 2019/5/2

import os, codecs
import jieba
import xlsxwriter
from collections import Counter

def get_words(txt):
    #进行分词计数并通过结果存在一个Dic中
    seg_list = jieba.cut(txt)
    c = Counter()
    WordToRate = {}
    #将分词进行频率计数
    for x in seg_list:
        if len(x) > 1 and x != '\r\n':
            c[x] += 1
    for (k, v) in c.most_common(100):
        WordToRate[k] = v
        print('%s%s %s  %d' % ('  ' * (5 - len(k)), k, '*' * int(v / 3), v))
    return WordToRate

def print_Excel(dic, Filename):
    #将dic中的内容保存在Filename.xlsx中
    workbook = xlsxwriter.Workbook( Filename +  '.xlsx')
    worksheet = workbook.add_worksheet()
    #设置起始的row和col
    row = 0
    col = 0
    #将字典内容迭代保存
    for item in (dic):
        worksheet.write(row, col, item)
        worksheet.write(row, col + 1, dic[item])
        row += 1
    #计算总和(部分最多项)
    worksheet.write(row, 0, 'Total')
    worksheet.write(row, 1, '=SUM(B1:B4)')
    workbook.close()

if __name__ == '__main__':
    #读取UTF-8保存的中文文本文件并保存为txt变量
    with codecs.open('Political.txt', 'r', 'utf8') as f:
        txtP = f.read()
    with codecs.open('Non-Political.txt', 'r', 'utf8') as f:
        txtNP = f.read()
    WordToRateP = get_words(txtP)
    WordToRateNP = get_words(txtNP)
    #写入Excel文件中
    print_Excel(WordToRateP, 'PoliticalRate')
    print_Excel(WordToRateNP, 'Non-PoliticalRate')
