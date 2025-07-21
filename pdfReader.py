# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 17:03:43 2021

@author: SKOTIYAL
"""


import PyPDF2

my_file = open('1010618411_feb.pdf','rb')

pdf_reader = PyPDF2.PdfFileReader(my_file)
print(pdf_reader.numPages)

page_one =pdf_reader.getPage(0)
print(page_one.extractText())

for i in range(pdf_reader.numPages):
    page=pdf_reader.getPage(i)
    print(page.extractText())