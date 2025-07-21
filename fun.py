# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 05:47:22 2021

@author: SKOTIYAL
"""

#required arg
# keyword arg
# default arg

def sum(a,b):
    return a+b

def mul(a,b=1): #wrong (a=1,b),as once we placed default value all the arg after that should have default value
    return(a*b)


print(sum(10,20)) #
print(sum(b=20,a=10))# this are keyword argument, can give in any order