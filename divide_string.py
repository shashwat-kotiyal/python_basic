# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 18:30:03 2021

@author: SKOTIYAL
"""


a = "abcdegf"


def divideString(string,3):
    str_size = len(string)
    
    part_size = string/3
    k=0
    for i in string:
        if k%part_size==0:
            