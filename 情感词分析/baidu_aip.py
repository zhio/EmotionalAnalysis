# from aip import AipNlp
# import time
# APP_ID = '14317515'
# API_KEY = 'LrcHE92DqsfEVpHlBh4GCzTB'
# SECRET_KEY = '13b51OZ4URH3AAx1o4LvPUSb3qG8ynp0'
#
# client = AipNlp(APP_ID,API_KEY,SECRET_KEY)
#
#
# text = "苹果是一家伟大的公司"
#
# """ 调用情感倾向分析 """
# def get_emotion(text):
#     response = client.sentimentClassify(text)
#     sentiment = response['items'][0]
#     positive = sentiment['positive_prob']
#     confidence = sentiment['confidence']
#     negative = sentiment['negative_prob']
#     sentiments = sentiment['sentiment']
#     print(f"正向:{positive},负向:{negative},可信度:{confidence},情感:{sentiments}")
#     return sentiment
#
# def get_text(path):
#     with open(path, 'r') as f:
#         data = f.readlines()
#     s = []
#     a = 0
#     for key, i in enumerate(data):
#         if i[0].isdigit():
#             text = ''.join(data[a:key]).replace('\n', '')
#             a = key
#             s.append(text)
#     return s
# if __name__ == '__main__':
#     path = 'juben.txt'
#     text = get_text(path)
#     flag = 1
#     for i in text:
#         get_emotion(i)
#         flag+=1
#         if flag%5==0:
#             time.sleep(5)
import xmnlp
doc = """自然语言处理: 是人工智能和语言学领域的分支学科。
在这此领域中探讨如何处理及运用自然语言；自然语言认知则是指让电脑“懂”人类的语言。 
自然语言生成系统把计算机数据转化为自然语言。自然语言理解系统把自然语言转化为计算机程序更易于处理的形式。"""

print(xmnlp.seg(doc, hmm=True))
