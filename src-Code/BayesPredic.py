#! python3
# -*- coding: utf-8 -*-
# Create by Hantong Liu 2019/5/2

import os, codecs
import jieba
from collections import Counter
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

#使用中文分词将所得新闻文段进行分词处理
def Predic(txt):
    #进行分词计数并通过结果存在一个字典中
    seg_list = jieba.cut(txt)
    c = Counter()
    WordToNumber = {}
    #将分词进行频率计数
    for x in seg_list:
        if len(x) > 1 and x != '\r\n':
            c[x] += 1
    for (k, v) in c.most_common(100):
        WordToNumber[k] = v
    #将两个Excel文件打开并读取成两个字典
    Political_df = pd.read_excel('PoliticalRate.xlsx', sheetname='Sheet1')
    NonPolitical_df = pd.read_excel('Non-PoliticalRate.xlsx', sheetname='Sheet1')
    Political_Dic = {}
    NonPolitical_Dic = {}
    for i in Political_df.index:
        Political_Dic[Political_df['Word'][i]] = Political_df['Number'][i]
    for i in NonPolitical_df.index:
        NonPolitical_Dic[NonPolitical_df['Word'][i]] = NonPolitical_df['Number'][i]
    #寻找两个dic中是否存在新闻语段的词语，并据此计算后验概率
    #首先定义概率的一个列表
    ProbabilityList = []
    for i in WordToNumber:
        if( i in Political_Dic and i in NonPolitical_Dic):
            #如果两个划分中都存在这个词，则利用贝叶斯公式计算是政治的概率
            P_A_B = Political_Dic[i] / Political_Dic['Total']
            P_A_NonB = NonPolitical_Dic[i] / NonPolitical_Dic['Total']
            P_B = 0.5
            P_NonB = 0.5
            Probability = ((P_A_B*P_B)/(P_A_B*P_B + P_A_NonB * P_NonB))
        elif(i in Political_Dic and ~(i in NonPolitical_Dic)):
            #如果只在政治划分中出现过，那么是政治的概率为1
            Probability = 1
        elif(i in NonPolitical_Dic and ~(i in Political_Dic)):
            #如果只在非政治划分中出现过，那么出现过的概率为零
            Probability = 0
        else:
            print("<" + i + ">：词语无效" )
        print("根据词语<" + i + ">推断的政治性新闻概率为" + str(Probability))
        ProbabilityList.append(Probability)
    #计算得到平均后验概率
    sum = 0
    for i in ProbabilityList:
        sum += i
    print(sum)
    print(len(ProbabilityList))
    PoliticalPredic = sum / len(ProbabilityList)
    return PoliticalPredic

if __name__ == '__main__':
    with codecs.open('PoliticalCopy.txt', 'r', 'utf8') as f:
        txtP = f.read()
    Probability = Predic(txtP)
    print("这个新闻是政治性内容的概率为：" + str(Probability))