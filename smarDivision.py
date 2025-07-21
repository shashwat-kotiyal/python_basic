# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 13:39:48 2021

@author: SKOTIYAL
"""


def smartdiv(div):
    def inner():
        if (a>b):
            r = div(a,b)
            return r
        if(b>a):
            r =div(b,a)
            return r
    return inner

def div(a,b):
    c = a/b
    return c

div(a,b) = smartdiv(div(a,b))
d = div
print(d)



