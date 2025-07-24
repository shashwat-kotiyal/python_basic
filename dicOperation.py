# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 08:57:39 2021

@author: SKOTIYAL
"""

"""
que: You have two dictionaries and want to find out what they might have in common 
(same keys, same values, etc.).

"""
dic1 = {'x':2,'y':3,'z':5}
dic2 = {'x':2,'y':5,'w':8}

#comman keys

print(f"common eys in dic1 and dic2 : {dic1.keys() & dic2.keys()}")

#comman key value pairs

print(f"common items in dic1 and dic2 : {dic1.items()& dic2.items()}")

#keys in a that are not in b

print(f" key not in  : {dic1.keys() - dic2.keys()}")

"""
Make a new dictionary with certain keys removed
"""

dic3 = {key:dic1[key] for key in dic1.keys()-{'z','w'}}
print(dic3)
