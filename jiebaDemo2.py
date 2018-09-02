'''
盗墓笔记实战
'''
import jieba.analyse
# 中文读取的时候最好使用rb
fileContent=open("daomu.txt",'rb').read().decode("utf-8","ignore")
tag = jieba.analyse.extract_tags(fileContent, 20)
print(tag)
