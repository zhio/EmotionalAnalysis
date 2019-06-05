import jieba
import numpy as np
import pandas as pd

nodic = pd.read_excel('/Users/wks/Desktop/情绪词典/否定词表.xlsx')
fc_dic = pd.read_excel("/Users/wks/Desktop/情绪词典/程度副词表.xlsx")
em_dic = pd.read_excel("/Users/wks/Desktop/情绪词典/情感词汇.xlsx")

no_list = []
for key in nodic['否定词汇']:
    no_list.append(key)

LE = ['PA','PE']
HAO = ['PD','PH','PG','PB','PK']
NU = ['NBA']
AI = ['NB','NJ','NH','PF']
JU = ['NI','NC','NG']
E = ['NE','ND','NN','NK','NL']
JIN = ['PC']
def num(k):
    if k in LE:
        k = '乐'
    elif k in HAO:
        k = '好'
    elif k in NU:
        k = '怒'
    elif k in AI:
        k = '哀'
    elif k in JU:
        k = '惧'
    elif k in E:
        k = '恶'
    elif k in JIN:
        k = '惊'
    return k

em_dic['new'] = em_dic['情感分类'].apply(num)

ems_dic = em_dic[['词语','强度','new']]

def getcut(sentence):
    seg = jieba.cut(sentence)
    seg_list = list(seg)
    print(seg_list)
    return seg_list
def judgeodd(num):
    if num % 2 == 0:
        return 'even'
    else:
        return 'odd'
def getemtion(seg_list):
    a = 0
    i = 0
    keys = []
    word_list = []
    for word in seg_list:
        b = 0
        if len(word)>1:
            try:
                ds = ems_dic.loc[[ems_dic[ems_dic.词语 == word].index[0]]]
                word_value = ds.强度.values[0]
                word_key = ds.new.values[0]
                for w in seg_list[a:i]:
                    try:
                        fc_flag = fc_dic.loc[[fc_dic[fc_dic.程度副词 == w].index[0]]]
                        fc_value = fc_flag.权值.values[0]
                        word_value *= fc_value
                        print(fc_value)
                    except:
                        pass
                    if w in no_list:
                        b += 1
                        print(b)
                if judgeodd(b) == 'odd':
                    word_value *= -1.0
                if word_value < 0:
                    if word_key == '乐':
                        word_key = '哀'
                        word_value = abs(word_value)
                    elif word_key == '好':
                        word_key = '恶'
                        word_value = abs(word_value)
                    elif word_key == '哀':
                        word_key = '乐'
                        word_value = abs(word_value)
                    elif word_key == '恶':
                        word_key = '好'
                        word_value = abs(word_value)
                    else:
                        word_value = 0.1

                a = i + 1
                print(word,word_key,word_value)
                word_list.append([word_key,word_value])
                #word_list.append([ds.词语.values[0],ds.强度.values[0],ds.new.values[0]])
                keys.append(i)
            except:
                pass
        i += 1
    print(word_list)
    pand_s = pd.DataFrame(word_list,columns=['情绪', '分数'])
    return pand_s

if __name__ == '__main__':
    sentence = '我喜欢这个手机'
    seg = getcut(sentence)
    print(getemtion(seg))