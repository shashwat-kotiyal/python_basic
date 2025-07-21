# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 16:34:54 2021

@author: skotiyal
"""
import os, sys

mydict ={"one":1,"two":2}

import pickle
#pickling for prg readable

pickle.dump(mydict,open('mydict.pickle','wb'))
#shuould be binary mode, bin file cant read as text file

print(os.listdir())

print(os.system("!cat mydict.pickle"))

res =pickle.load(open('mydict.pickle','rb'))
print(res)

import json
#multi purpose
with open('data.json','w') as outfile:
    json.dump(res,outfile)
    
with open('data.json','r') as outfile:
    res2=json.load(outfile)
    
print(res2)

import yaml
#human frendly
with open('data.yaml','w') as yamlfile:
    yaml.safe_dump(res2,yamlfile)
    
with open("data.yaml",'r') as yamlfile:
    res3= yaml.safe_load(yamlfile)
    
print(res3)


