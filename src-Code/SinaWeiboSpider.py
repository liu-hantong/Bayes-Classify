# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# Create by Hantong Liu, 2019/5/1

import urllib.request
import json

#央视新闻<国际新闻>官方微博ID
id='6473970060'

#设置代理IP
proxy_addr="122.241.72.191:808"

#定义页面打开函数
#使用urllib及request构造访问头并对页面进行访问
def use_proxy(url,proxy_addr):
    req=urllib.request.Request(url)
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
    proxy=urllib.request.ProxyHandler({'http':proxy_addr})
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(req).read().decode('utf-8','ignore')
    return data

#获取微博主页的containerid，爬取微博内容时需要此id
def get_containerid(url):
    data=use_proxy(url,proxy_addr)
    content=json.loads(data).get('data')
    for data in content.get('tabsInfo').get('tabs'):
        if(data.get('tab_type')=='weibo'):
            containerid=data.get('containerid')
    return containerid

#获取微博内容信息,并保存到文本中
#一共获取500条微博信息
def get_weibo(id,file):
    i=1
    while True:
        url='https://m.weibo.cn/api/container/getIndex?type=uid&value='+id
        weibo_url='https://m.weibo.cn/api/container/getIndex?type=uid&value='+id+'&containerid='+get_containerid(url)+'&page='+str(i)
        try:
            data=use_proxy(weibo_url,proxy_addr)
            content=json.loads(data).get('data')
            cards=content.get('cards')
            if(i <= 500):
                for j in range(len(cards)):
                    print("-----正在爬取第"+str(i)+"条-----")
                    card_type=cards[j].get('card_type')
                    if(card_type==9):
                        mblog=cards[j].get('mblog')
                        text=mblog.get('text')
                        text = text.split('<')[0]     #分割<符号，目的在于获取信息为纯文本，不包括Url
                        if (text):                    #如果排除Url后的文本非空，则保存在文本中
                            with open(file,'a',encoding='utf-8') as fh:
                                fh.write(str(i) + ": " + text + "\n\n")
                                i+=1
                    if(i > 500):
                        break
            else:
                break
        except Exception as e:
            print(e)
            pass

if __name__=="__main__":
    file= "Weibos"+".txt"  #新闻微博聚合文件
    get_weibo(id,file)     #从微博id为id的用户中爬取微博并保存