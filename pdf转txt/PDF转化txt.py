'''
使用pdfminer3k读取pdf文档
'''
import os
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams

IN_PUT_PATH = '22.pdf'
OUT_PUT = '火锅英雄.txt'
fp = open(IN_PUT_PATH, 'rb')  # 打开一个pdf文档
parser = PDFParser(fp)  # 创建一个与pdf文档关联的解析器对象
doc = PDFDocument()  # 创建一个pdf文档对象, 用于存储文档结构
parser.set_document(doc)  # 将解析器与文档对象关联
doc.set_parser(parser)
doc.initialize('')  # 初始化文档

resource = PDFResourceManager()  # 创建一个pdf资源管理器对象，用于存储共享资源
laparam = LAParams()  # 参数分析器
device = PDFPageAggregator(resource, laparams=laparam)  # 创建pdf页面聚合器对象
interpreter = PDFPageInterpreter(resource, device)  # 创建pdf解释器对象

for page in doc.get_pages():  # 使用文档对象得到页面的集合
    interpreter.process_page(page)  # 使用页面解析器读取内容
    layout = device.get_result()  # 使用聚合器来获取内容
    for out in layout:
        if hasattr(out, 'get_text'):
            print(out.get_text())
            f = open(OUT_PUT,'a+')
            f.write(out.get_text())