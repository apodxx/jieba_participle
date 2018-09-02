import jieba

sentence = "我喜欢上海东方明珠"
# cut(句子变量，分词模式（1 全模式，2精准模式(默认)）)
# 1 全模式
wordArr = jieba.cut(sentence, cut_all=True)
for word in wordArr:
    print(word)
print("--------")
# 2精准模式(默认)
wordArr1 = jieba.cut(sentence, cut_all=False)
for word in wordArr1:
    print(word)
print("--------")
#  3搜索引擎分词模式
wordArr2 = jieba.cut_for_search(sentence)
for word in wordArr2:
    print(word)
print("--------")

'''
# flag词性
# word词语
    a:形容词
    c:连词
    d:副词
    e:叹词
    f:方位词
    i:成语
    m:数词
    n:名词
    nr:人名
    ns:地名
    nt:机构团体
    nz:其他专有词语
    p:介词
    r:代词
    t:时间
    u:助词
    v:动词
    vn:动名词
    w:标点符号
    un:未知词语
    
'''
# 词性标注
# flag词性
# word词语
import jieba.posseg

sen = "医院"
wordType = jieba.posseg.cut(sen)
for item in wordType:
    print(item.word + "--" + item.flag)
print("--------")

# 加载自定义词典（加载到了内存中）
jieba.load_userdict("E:/Users/Administrator/Anaconda3/Lib/site-packages/jieba/dict2.txt")
sentence2 = "天善智能传智播客文都教育"
wordArr3 = jieba.posseg.cut(sentence2)
for w in wordArr3:
    print(w.word + "--" + w.flag)
print("--------")

# 词频更改
sentence = "我喜欢上海东方明珠"

wordArr4 = jieba.cut(sentence)
for word in wordArr4:
    print(word)
print("------------")

# 更改"上海东方"为一个词(存疑)
jieba.suggest_freq("上海东方", True)
wordArr5 = jieba.cut(sentence)
for word in wordArr5:
    print(word)
print("------------")

#提取关键词
import jieba.analyse
words = '我喜欢上海东方明珠'
tag = jieba.analyse.extract_tags(words, 2)
print(tag)
print("------------")

# 返回词语的位置(精准模式)
wordOrder=jieba.tokenize(sentence)
for word in wordOrder:
    print(word)
print("------------")

# 返回词语的位置（搜索引擎模式）
wordOrder=jieba.tokenize(sentence,mode="search")
for word in wordOrder:
    print(word)


print("------------")