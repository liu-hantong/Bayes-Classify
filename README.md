# 基于贝叶斯公式的特定文本性质判断与分类
## 介绍
尝试利用python语言结合特定文本（爬虫获取的微博或新闻摘要等）实现语言性质的分析，根据语言用词等方面倒退文本是否具有侮辱和诽谤性质，并根据用语程度推断是否需要进行删除处理等，关于具体方法和分析请参考paper文件夹下的[论文原文](https://github.com/llht/Bayes-Classify/blob/master/paper/%E5%9F%BA%E4%BA%8E%E8%B4%9D%E5%8F%B6%E6%96%AF%E5%85%AC%E5%BC%8F%E7%9A%84%E7%89%B9%E5%AE%9A%E6%96%87%E6%9C%AC%E6%80%A7%E8%B4%A8%E5%88%A4%E6%96%AD%E4%B8%8E%E5%88%86%E7%B1%BB.pdf)，本文为修读《概率论与数理统计》课程时完成的期中大作业
## 文件说明
1. 论文原文请直接查看[paper](https://github.com/llht/Bayes-Classify/tree/master/paper)文件夹，其中md扩展名文件推荐使用`Typora`软件查看，pdf扩展名文件使用`Acrobat Reader DC`软件查看
2. [src-Code](https://github.com/llht/Bayes-Classify/tree/master/src-Code)文件夹为进行文本判定时使用的源代码
3. [src-Text](https://github.com/llht/Bayes-Classify/tree/master/src-Text)文件夹为进行模型训练时使用的源文本
4. [Excel](https://github.com/llht/Bayes-Classify/tree/master/Excel)文件夹中文件为论文中使用的统计数据
