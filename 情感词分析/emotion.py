import jieba
import numpy as np
import pandas as pd
from scipy import optimize
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Arial Unicode Ms']
class emotion():
    def __init__(self):
        self.nodic = pd.read_excel('/Users/wks/Desktop/情绪词典/否定词表.xlsx')
        self.fc_dic = pd.read_excel("/Users/wks/Desktop/情绪词典/程度副词表.xlsx")
        self.em_dic = pd.read_excel("/Users/wks/Desktop/情绪词典/情感词汇.xlsx")
        self.no_list = []
        for key in self.nodic['否定词汇']:
            self.no_list.append(key)

        self.em_dic['new'] = self.em_dic['情感分类'].apply(self.num)

        self.ems_dic = self.em_dic[['词语', '强度', 'new']]

    def num(self,k):
        #将字典中的十四种情绪转化为七种
        LE = ['PA', 'PE']
        HAO = ['PD', 'PH', 'PG', 'PB', 'PK']
        NU = ['NBA']
        AI = ['NB', 'NJ', 'NH', 'PF']
        JU = ['NI', 'NC', 'NG']
        E = ['NE', 'ND', 'NN', 'NK', 'NL']
        JIN = ['PC']
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

    def getcut(self,sentence):
        #分词
        seg = jieba.cut(sentence)
        seg_list = list(seg)
        print(f'分词结果为：{seg_list}')
        return seg_list
    def judgeodd(self,num):
        #判断奇偶，用于否定词判断
        if num % 2 == 0:
            return 'even'
        else:
            return 'odd'
    def getemtion(self,seg_list):
        a = 0
        i = 0
        keys = []
        word_list = []
        for word in seg_list:
            b = 0
            if len(word)>1:
                try:
                    ds = self.ems_dic.loc[[self.ems_dic[self.ems_dic.词语 == word].index[0]]]
                    word_value = ds.强度.values[0]
                    word_key = ds.new.values[0]
                    for w in seg_list[a:i]:
                        try:
                            fc_flag = self.fc_dic.loc[[self.fc_dic[self.fc_dic.程度副词 == w].index[0]]]
                            fc_value = fc_flag.权值.values[0]
                            word_value *= fc_value
                        except:
                            pass
                        if w in self.no_list:
                            b += 1
                            # print('否定词个数为:',b)

                    if self.judgeodd(b) == 'odd':
                        word_value *= -1.0
                    #当某种情绪出现负数，转化为相反情绪
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

    def fenxi_emotion(self,pand_s):
        #统计情绪
        wordlist = [['乐',0.],['好',0.],['怒',0.],['哀',0.],['惧',0.],['恶',0.],['惊',0.]]
        pads = pd.DataFrame(wordlist, columns=['情绪', '分数'])
        s_list = [pads, pand_s]
        ss = pd.concat(s_list)
        fx_emotion = ss.groupby(by = '情绪').sum()

        fx_em = fx_emotion.sort_values('分数',ascending=False)
        return fx_em

    def func(self,listTemp,n):
        #将列表分段
        for i in range(0,len(listTemp),n):
            yield listTemp[i:i+n]

    def get_text_comment(self,path):
        #一般文本按行分成N段
        with open(path,'r') as f:
            data =f.readlines()
        n = len(data)//20
        temp = self.func(data,n)
        s = []
        for i in temp:
            text = ''.join(i).replace('\n','').replace(' ','')
            s.append(text)
        # for i in range(len(s)):
        #     text = ' '.join(s[i:i+10])
        #     yield text
        return s

        return text
    def get_text(self,path):
        #有序号文本按场景分段
        with open(path, 'r') as f:
            data = f.readlines()
        s = []
        ss = []
        a = 0
        for key, i in enumerate(data):
            if i[0].isdigit():
                text = ''.join(data[a:key]).replace('\n', '')
                a = key
                s.append(text)
        # for i in range(len(s)):                     #扫描窗口
        #     text = ' '.join(s[i:i + 5])
        #     ss.append(text)
        return s

    def get_cumsum_line(self,path):
        s = self.get_text_comment(path)
        df = pd.DataFrame(columns=['乐','好','怒','哀','惧','恶','惊'])
        for sentence in s:
            seg = self.getcut(sentence)
            fx_ems = self.getemtion(seg)
            # print(fenxi_emotion(fx_ems))
            dfs = self.fenxi_emotion(fx_ems)['分数']
            df = df.append(dfs,ignore_index=True)
        df2 = df.cumsum()
        df2.plot()
        plt.show()
    def get_leore_line(self,path):
        s = self.get_text_comment(path)
        df = pd.DataFrame(columns=['乐','好','怒','哀','惧','恶','惊'])
        for sentence in s:
            seg = self.getcut(sentence)
            fx_ems = self.getemtion(seg)
            # print(fenxi_emotion(fx_ems))
            dfs = self.fenxi_emotion(fx_ems)['分数']
            print(dfs)
            df = df.append(dfs,ignore_index=True)
        print(df)
        df['好恶曲线'] = df['好']-df['恶']
        df['乐哀曲线'] = df['乐']-df['哀']
        df['好恶哀乐'] = df['好恶曲线'] + df['乐哀曲线']
        # dfs = pd.DataFrame([df['好恶曲线'],df['乐哀曲线']])
        # dfs = dfs.T
        df['好恶哀乐'].plot()
        plt.show()
        self.get_nihe(df)
        return df

    def fmax(self,x,a,b,c):
        return a*np.sin(x*np.pi/6+b)+c

    def get_nihe(self,df):

        ymax = df['好恶哀乐'].to_numpy()
        n = len(ymax)
        x = np.arange(1,n+1,1)
        x1 = np.arange(1,n+1,0.01)
        fita, fitb = optimize.curve_fit(self.fmax, x, ymax, [1, 1, 1])
        plt.plot(x, ymax)
        plt.plot(x1, self.fmax(x1, fita[0], fita[1], fita[2]))
        plt.show()
if __name__ == '__main__':
    path = '湄公河行动.txt'
    emotions = emotion()
    df = emotions.get_leore_line(path) #获取波动曲线
    # emotions.get_cumsum_line(path) #获取累加曲线


