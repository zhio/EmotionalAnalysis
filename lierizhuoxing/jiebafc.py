import jieba
import pkuseg
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
LE = ['PA','PE']
HAO = ['PD','PH','PG','PB','PK']
NU = ['NA']
AI = ['NB','NJ','NH','PF']
JU = ['NI','NC','NG']
E = ['NE','ND','NN','NK','NL']
JIN = ['PC']
def num(lis):
    lis = np.array(lis)
    key = np.unique(lis)
    result = {}
    for k in key:
        mask = (lis == k)
        list_new = lis[mask]
        v = list_new.size
        if k in LE:
            k = 'LE'
        elif k in HAO:
            k = 'HAO'
        elif k in NU:
            k = 'NU'
        elif k in AI:
            k = 'AI'
        elif k in JU:
            k = 'JU'
        elif k in E:
            k = 'E'
        elif k in JIN:
            k = 'JIN'
        result[k] = v
    return result
with open('juben.txt','r') as f:
    data = f.readlines()
s = []
a = 0
for key,i in enumerate(data):
    if i[0].isdigit():
        text = ''.join(data[a:key]).replace('\n','')
        a = key
        s.append(text)
myrows = []
# num = 0
# for line in s:
#     myrows.append([num,line])
#     num = num + 1
# print(myrows[:3])

# df = pd.DataFrame(myrows)
# df.head()
# df.columns = ['line', 'text']
# df.to_csv('data.csv',index=False)

dic = pd.read_excel('em_data.xlsx')
i = 0
words = []
good = []
for line in s:
    seg_list = jieba.cut(line,cut_all=True)
    # print(list(seg_list))
    word = []
    for seg in list(seg_list):
        if len(seg)>1:
            try:
                flag = seg
                ds = dic.loc[[dic[dic.词语 == flag].index[0]]]
                print(ds.词语.values[0],ds.情感分类.values[0])
                word.append(ds.情感分类.values[0])
                i = i + 1
            except IndexError:
                pass
    asss = num(word)
    words.append(word)
    good.append(asss)
print(words)
print(asss)
print(good)
print(f"总共找到{i}个关键词")
wdlen = []
for wd in words:
    wd_len =  len(wd)
    wdlen.append(wd_len)
print(wdlen)

key_word = [0, 0, 1, 0, 1, 3, 7, 1, 11, 0, 3, 1, 3, 2, 3, 19, 0, 0, 0, 14, 3, 9, 28, 1, 3, 1, 2, 2, 4, 9, 1, 0, 5, 1, 45, 0, 0, 1, 0, 2, 6, 0, 2, 6, 0, 2, 0, 2, 0, 2, 0, 3, 2, 1, 1, 5, 1, 4, 3, 1, 3, 11, 3, 0, 0, 0, 1, 1, 0, 21, 1, 12, 2, 1, 0, 2, 4, 4, 0, 3, 0, 6, 2, 0, 0, 9, 0, 4, 4, 15, 14, 21, 2, 1, 3, 9, 6, 21, 4, 4, 2, 1, 5, 2, 0, 0, 0, 6, 1, 7, 9, 3, 17, 6, 1, 0, 1, 1, 3, 1, 3, 4, 1, 3, 12, 19, 8, 0, 14, 5, 11, 16, 0, 5, 1, 22, 13, 5, 5, 0, 1, 1, 0, 11]
# types = [[], [], ['NI'], [], ['ND'], ['ND', 'PH', 'NI'],
#          ['PF', 'PA', 'NE', 'PA', 'NI', 'NE', 'NC'], ['PH'],
#          ['ND', 'NN', 'NI', 'ND', 'PK', 'NN', 'PC', 'ND', 'PH', 'PB', 'PK'],
#          [], ['ND', 'NC', 'ND'], ['NN'], ['NN', 'NI', 'PG'], ['NN', 'ND'],
#          ['NL', 'PB', 'PA'], ['PC', 'NC', 'NN', 'NC', 'PH', 'NC', 'NC', 'NN', 'NN', 'NL', 'NL', 'NI', 'PH', 'PD', 'NL', 'NN', 'NE', 'NL', 'PD'], [], [], [], ['PC', 'NE', 'PH', 'NN', 'NE', 'PC', 'NN', 'PD', 'NH', 'PH', 'NN', 'NH', 'PH', 'PH'], ['NL', 'NJ', 'NE'],
#          ['NL', 'PB', 'PD', 'NN', 'PH', 'NE', 'PH', 'PH', 'PG'],
#          ['NE', 'NN', 'NN', 'PH', 'NI', 'PA', 'PH', 'PA', 'NN', 'PH', 'PD', 'NC', 'NC', 'NC', 'NI', 'NC', 'PA', 'NN', 'NN', 'PE', 'NE', 'NL', 'NL', 'NL', 'PB', 'PH', 'PH', 'PB'], ['ND'], ['PH', 'NN', 'NL'], ['NN'], ['PH', 'PB'], ['NG', 'NI'], ['NI', 'NE', 'NN', nan], ['PH', 'NN', 'NN', 'PH', 'NN', 'NC', 'NJ', 'NC', 'PB'], ['PH'], [], ['NN', 'ND', 'PG', 'PD', 'NE'], ['NE'], ['NN', 'PH', 'PH', 'PH', 'PH', 'PD', 'PD', 'PD', 'NN', 'PD', 'PA', 'PA', 'PA', 'PH', 'ND', 'NE', 'PF', 'PD', 'NI', 'NI', 'NI', 'PC', 'NN', 'NN', 'NL', 'PH', 'PD', 'NB', 'ND', 'ND', 'PG', 'NN', 'PH', 'ND', 'NC', 'NC', 'PB', 'NN', 'ND', 'PD', 'NE', 'NG', 'PD', 'PD', 'NL'], [], [], ['NI'], [], ['PH', 'PA'], ['NN', 'NN', 'NB', 'NN', 'NB', 'NN'], [], [nan, 'PK'], ['NC', 'PA', 'NE', 'NC', 'NC', 'PB'], [], ['PA', nan], [], ['PC', 'PC'], [], ['NB', 'NB'], [], ['NB', 'ND', 'NI'], ['NI', 'NC'], ['NB'], ['PC'], ['ND', 'NB', 'ND', 'NL', 'NL'], ['NC'], ['PC', 'NB', 'NE', 'NL'], ['NI', 'NL', 'NE'], ['NE'], ['ND', 'PA', 'NN'], ['NE', 'PH', nan, 'ND', 'ND', 'PK', 'NH', 'NE', 'NL', 'NB', 'ND'], ['ND', 'PK', 'NI'], [], [], [], ['PH'], ['PD'], [], ['NB', 'PB', 'PH', 'NN', 'NN', 'NL', 'NN', 'NN', 'NL', 'NN', 'NN', 'NN', 'NI', 'NB', 'NN', 'PB', 'NH', 'NC', 'NE', 'NB', 'NB'], ['NI'], ['PK', 'PH', 'PA', 'NN', 'PE', 'PD', 'NN', 'PB', 'PB', 'PH', 'NN', 'PA'], ['NN', 'NE'], ['NC'], [], ['NL', 'PH'], ['PA', 'PA', 'ND', 'NN'], ['ND', 'NB', 'PK', 'PH'], [], ['NC', 'NC', 'PE'], [], ['NI', 'NB', 'NB', 'PF', 'PC', 'NN'], ['PH', 'PK'], [], [], ['NN', 'PA', 'PH', 'PK', 'NL', 'PH', 'PH', 'NC', 'NC'], [], ['PD', 'PD', 'PD', 'PD'], ['PG', 'NL', 'PD', 'NN'], ['PD', 'PD', 'PD', 'PD', 'PD', 'PD', 'NE', 'PD', 'PD', 'NE', 'PH', 'PD', 'PD', 'PD', 'PD'], ['NE', 'PH', 'PA', 'PD', 'ND', 'NL', 'PA', 'ND', 'PB', 'NJ', 'NJ', 'PK', 'NN', 'NL'], ['ND', 'PH', 'NB', 'NC', 'PH', 'PB', 'NL', 'PA', 'PG', 'PF', 'PF', 'NL', 'NL', 'NN', 'PK', 'PK', 'PH', 'NN', 'PH', 'NN', 'NE'], ['PH', 'PB'], ['PG'], ['PB', 'NN', 'NB'], ['PB', 'PA', 'PE', 'PA', 'PA', 'PH', 'PB', 'NI', 'PB'], ['PA', 'NB', 'PH', 'NB', 'PH', 'PA'], ['PG', 'PB', 'PH', 'PH', 'PG', 'NJ', 'NN', 'NN', 'PH', 'PH', 'PE', 'PG', 'NN', 'NN', 'NN', 'PA', 'PG', 'PH', 'PH', 'ND', 'PH'], ['NI', 'NN', 'NG', 'PD'], ['NC', 'PC', 'PH', 'PC'], ['NC', 'PB'], ['PA'], ['NL', 'NL', 'NN', 'NL', 'NN'], ['NL', 'NE'], [], [], [], ['NN', 'NL', 'PD', 'PD', 'NN', 'NI'], ['NE'], ['PB', 'NE', 'PK', 'PD', 'NI', 'NC', 'NC'], ['PD', 'PD', 'NN', 'NH', 'NH', 'PD', 'PD', 'PF', 'NH'], ['PA', 'PH', 'PG'], ['PB', 'NG', 'PD', 'NN', 'PG', 'PC', 'NL', 'NL', 'PG', 'PE', 'NL', nan, 'NE', 'NJ', 'NJ', 'NB', 'NB'], ['NN', 'NN', 'ND', 'PE', 'NN', 'NH'], ['NB'], [], ['PH'], ['NB'], ['NB', 'NN', 'NN'], ['NE'], ['NN', 'PH', 'PH'], ['PK', 'NN', 'PH', 'NI'], ['PH'], ['PH', 'NN', 'NI'], ['PH', 'NN', 'PH', 'NN', 'PC', 'NI', 'PH', 'NN', 'NE', 'ND', 'NB', 'NN'], ['NB', 'NC', 'NC', 'NH', 'NN', 'PH', 'NC', 'ND', 'ND', 'PE', 'PC', 'PH', 'PK', 'NE', 'PK', 'PA', 'NN', 'NN', 'PH'], ['PA', 'PG', 'PH', 'NN', 'PD', 'NN', 'PA', 'PA'], [], ['NE', 'PH', 'PD', 'PH', 'NH', 'PG', 'NH', 'PG', 'PC', 'PA', 'PK', 'PH', 'PA', 'NB'], ['NB', 'PG', 'PG', 'NB', 'NN'], ['NL', nan, 'NL', 'NL', 'PA', 'NN', 'PA', 'PH', 'PA', 'NL', 'PA'], ['NB', 'PH', 'PG', 'NL', 'PK', nan, 'NN', 'PK', 'PA', 'PH', 'PH', 'NB', 'PK', 'PH', 'PC', 'NB'], [], ['NJ', 'PA', 'NN', 'PA', 'PA'], ['PD'], ['PD', 'PD', 'NH', 'NE', 'ND', 'PH', 'NC', 'PH', 'NE', 'PA', 'PB', 'NG', 'PK', 'NJ', 'PG', 'PG', 'PG', 'NL', 'PG', 'PG', 'NL', 'NE'], ['PD', 'PD', 'PD', 'PC', 'PD', 'NL', 'PD', 'NL', 'NB', 'NL', 'PH', 'PG', 'PD'], ['PG', 'NC', 'NN', 'PH', 'PA'], ['PD', 'PA', 'PH', 'PH', 'PD'], [], ['NL'], ['NB'], [], ['NN', 'PH', 'NJ', 'NJ', 'PH', 'PG', 'PH', 'PH', 'NL', 'PA', 'PA']]

# for ty in words:
#     print(num(ty))

good_word = [{}, {}, {'NI': 1}, {}, {'ND': 1}, {'ND': 1, 'NI': 1, 'PH': 1}, {'NC': 1, 'NE': 2, 'NI': 1, 'PA': 2, 'PF': 1}, {'PH': 1}, {'ND': 3, 'NI': 1, 'NN': 2, 'PB': 1, 'PC': 1, 'PH': 1, 'PK': 2}, {}, {'NC': 1, 'ND': 2}, {'NN': 1}, {'NI': 1, 'NN': 1, 'PG': 1}, {'ND': 1, 'NN': 1}, {'NL': 1, 'PA': 1, 'PB': 1}, {'NC': 4, 'NE': 1, 'NI': 1, 'NL': 4, 'NN': 4, 'PC': 1, 'PD': 2, 'PH': 2}, {}, {}, {}, {'NE': 2, 'NH': 2, 'NN': 3, 'PC': 2, 'PD': 1, 'PH': 4}, {'NE': 1, 'NJ': 1, 'NL': 1}, {'NE': 1, 'NL': 1, 'NN': 1, 'PB': 1, 'PD': 1, 'PG': 1, 'PH': 3}, {'NC': 4, 'NE': 2, 'NI': 2, 'NL': 3, 'NN': 5, 'PA': 3, 'PB': 2, 'PD': 1, 'PE': 1, 'PH': 5}, {'ND': 1}, {'NL': 1, 'NN': 1, 'PH': 1}, {'NN': 1}, {'PB': 1, 'PH': 1}, {'NG': 1, 'NI': 1}, {'NE': 1, 'NI': 1, 'NN': 1, 'nan': 1}, {'NC': 2, 'NJ': 1, 'NN': 3, 'PB': 1, 'PH': 2}, {'PH': 1}, {}, {'ND': 1, 'NE': 1, 'NN': 1, 'PD': 1, 'PG': 1}, {'NE': 1}, {'NB': 1, 'NC': 2, 'ND': 5, 'NE': 2, 'NG': 1, 'NI': 3, 'NL': 2, 'NN': 6, 'PA': 3, 'PB': 1, 'PC': 1, 'PD': 9, 'PF': 1, 'PG': 1, 'PH': 7}, {}, {}, {'NI': 1}, {}, {'PA': 1, 'PH': 1}, {'NB': 2, 'NN': 4}, {}, {'PK': 1, 'nan': 1}, {'NC': 3, 'NE': 1, 'PA': 1, 'PB': 1}, {}, {'PA': 1, 'nan': 1}, {}, {'PC': 2}, {}, {'NB': 2}, {}, {'NB': 1, 'ND': 1, 'NI': 1}, {'NC': 1, 'NI': 1}, {'NB': 1}, {'PC': 1}, {'NB': 1, 'ND': 2, 'NL': 2}, {'NC': 1}, {'NB': 1, 'NE': 1, 'NL': 1, 'PC': 1}, {'NE': 1, 'NI': 1, 'NL': 1}, {'NE': 1}, {'ND': 1, 'NN': 1, 'PA': 1}, {'NB': 1, 'ND': 3, 'NE': 2, 'NH': 1, 'NL': 1, 'PH': 1, 'PK': 1, 'nan': 1}, {'ND': 1, 'NI': 1, 'PK': 1}, {}, {}, {}, {'PH': 1}, {'PD': 1}, {}, {'NB': 4, 'NC': 1, 'NE': 1, 'NH': 1, 'NI': 1, 'NL': 2, 'NN': 8, 'PB': 2, 'PH': 1}, {'NI': 1}, {'NN': 3, 'PA': 2, 'PB': 2, 'PD': 1, 'PE': 1, 'PH': 2, 'PK': 1}, {'NE': 1, 'NN': 1}, {'NC': 1}, {}, {'NL': 1, 'PH': 1}, {'ND': 1, 'NN': 1, 'PA': 2}, {'NB': 1, 'ND': 1, 'PH': 1, 'PK': 1}, {}, {'NC': 2, 'PE': 1}, {}, {'NB': 2, 'NI': 1, 'NN': 1, 'PC': 1, 'PF': 1}, {'PH': 1, 'PK': 1}, {}, {}, {'NC': 2, 'NL': 1, 'NN': 1, 'PA': 1, 'PH': 3, 'PK': 1}, {}, {'PD': 4}, {'NL': 1, 'NN': 1, 'PD': 1, 'PG': 1}, {'NE': 2, 'PD': 12, 'PH': 1}, {'ND': 2, 'NE': 1, 'NJ': 2, 'NL': 2, 'NN': 1, 'PA': 2, 'PB': 1, 'PD': 1, 'PH': 1, 'PK': 1}, {'NB': 1, 'NC': 1, 'ND': 1, 'NE': 1, 'NL': 3, 'NN': 3, 'PA': 1, 'PB': 1, 'PF': 2, 'PG': 1, 'PH': 4, 'PK': 2}, {'PB': 1, 'PH': 1}, {'PG': 1}, {'NB': 1, 'NN': 1, 'PB': 1}, {'NI': 1, 'PA': 3, 'PB': 3, 'PE': 1, 'PH': 1}, {'NB': 2, 'PA': 2, 'PH': 2}, {'ND': 1, 'NJ': 1, 'NN': 5, 'PA': 1, 'PB': 1, 'PE': 1, 'PG': 4, 'PH': 7}, {'NG': 1, 'NI': 1, 'NN': 1, 'PD': 1}, {'NC': 1, 'PC': 2, 'PH': 1}, {'NC': 1, 'PB': 1}, {'PA': 1}, {'NL': 3, 'NN': 2}, {'NE': 1, 'NL': 1}, {}, {}, {}, {'NI': 1, 'NL': 1, 'NN': 2, 'PD': 2}, {'NE': 1}, {'NC': 2, 'NE': 1, 'NI': 1, 'PB': 1, 'PD': 1, 'PK': 1}, {'NH': 3, 'NN': 1, 'PD': 4, 'PF': 1}, {'PA': 1, 'PG': 1, 'PH': 1}, {'NB': 2, 'NE': 1, 'NG': 1, 'NJ': 2, 'NL': 3, 'NN': 1, 'PB': 1, 'PC': 1, 'PD': 1, 'PE': 1, 'PG': 2, 'nan': 1}, {'ND': 1, 'NH': 1, 'NN': 3, 'PE': 1}, {'NB': 1}, {}, {'PH': 1}, {'NB': 1}, {'NB': 1, 'NN': 2}, {'NE': 1}, {'NN': 1, 'PH': 2}, {'NI': 1, 'NN': 1, 'PH': 1, 'PK': 1}, {'PH': 1}, {'NI': 1, 'NN': 1, 'PH': 1}, {'NB': 1, 'ND': 1, 'NE': 1, 'NI': 1, 'NN': 4, 'PC': 1, 'PH': 3}, {'NB': 1, 'NC': 3, 'ND': 2, 'NE': 1, 'NH': 1, 'NN': 3, 'PA': 1, 'PC': 1, 'PE': 1, 'PH': 3, 'PK': 2}, {'NN': 2, 'PA': 3, 'PD': 1, 'PG': 1, 'PH': 1}, {}, {'NB': 1, 'NE': 1, 'NH': 2, 'PA': 2, 'PC': 1, 'PD': 1, 'PG': 2, 'PH': 3, 'PK': 1}, {'NB': 2, 'NN': 1, 'PG': 2}, {'NL': 4, 'NN': 1, 'PA': 4, 'PH': 1, 'nan': 1}, {'NB': 3, 'NL': 1, 'NN': 1, 'PA': 1, 'PC': 1, 'PG': 1, 'PH': 4, 'PK': 3, 'nan': 1}, {}, {'NJ': 1, 'NN': 1, 'PA': 3}, {'PD': 1}, {'NC': 1, 'ND': 1, 'NE': 3, 'NG': 1, 'NH': 1, 'NJ': 1, 'NL': 2, 'PA': 1, 'PB': 1, 'PD': 2, 'PG': 5, 'PH': 2, 'PK': 1}, {'NB': 1, 'NL': 3, 'PC': 1, 'PD': 6, 'PG': 1, 'PH': 1}, {'NC': 1, 'NN': 1, 'PA': 1, 'PG': 1, 'PH': 1}, {'PA': 1, 'PD': 2, 'PH': 2}, {}, {'NL': 1}, {'NB': 1}, {}, {'NJ': 2, 'NL': 1, 'NN': 1, 'PA': 2, 'PG': 1, 'PH': 4}]
