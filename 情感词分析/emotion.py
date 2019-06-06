import jieba
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Arial Unicode Ms']
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
    print(f'分词结果为：{seg_list}')
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
                    print('否定词个数为:',b)

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
            # print(f'情绪词为:{word},属于:{word_key},权值为{word_value}')
            word_list.append([word_key,word_value])
            #word_list.append([ds.词语.values[0],ds.强度.values[0],ds.new.values[0]])
            keys.append(i)
        except:
            pass
        i += 1
    # print(word_list)
    pand_s = pd.DataFrame(word_list,columns=['情绪', '分数'])
    return pand_s

def fenxi_emotion(pand_s):
    wordlist = [['乐',0.],['好',0.],['怒',0.],['哀',0.],['惧',0.],['恶',0.],['惊',0.]]
    pads = pd.DataFrame(wordlist, columns=['情绪', '分数'])
    s_list = [pads, pand_s]
    ss = pd.concat(s_list)
    fx_emotion = ss.groupby(by = '情绪').sum()

    fx_em = fx_emotion.sort_values('分数',ascending=False)
    return fx_em

def get_text(path):
    with open(path, 'r') as f:
        data = f.readlines()
    s = []
    a = 0
    for key, i in enumerate(data):
        if i[0].isdigit():
            text = ''.join(data[a:key]).replace('\n', '')
            a = key
            s.append(text)
    return s

if __name__ == '__main__':
    # sentence = '我也想过过儿过过的生活，我一点也不觉得有什么不好的地方'
    # seg = getcut(sentence)
    # print(getemtion(seg))
    path = 'juben.txt'
    s = get_text(path)
    df = pd.DataFrame(columns=['乐','好','怒','哀','惧','恶','惊'])
    for sentence in s:
        seg = getcut(sentence)
        fx_ems = getemtion(seg)
        # print(fenxi_emotion(fx_ems))
        dfs = fenxi_emotion(fx_ems)['分数']
        print(dfs)
        df = df.append(dfs,ignore_index=True)
    print(df)
    df2 = df.cumsum()
    df2.plat()
    plt.show()
