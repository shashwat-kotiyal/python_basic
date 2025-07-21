# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 04:54:58 2021

@author: SKOTIYAL
"""



tuple1 = ('ramya',27,'kavita',31,'ami',31)

print(tuple1.count(31)) #count no of time value display in tuple
print(tuple1.index('kavita'))# index of any value

tuple2 =('kriti',28)

tuple3= tuple1+tuple2
print(tuple3)

#insert at particular index, 2

tuple1 = tuple1[:2] +('shashwat',) +tuple1[2:] #if one element is there then need to put , in end else not
print(tuple1)
tuple1 = tuple1[:2] +('shashwat',29) +tuple1[2:]
print(tuple1)


#key and value can be of any data type
#key must be unique
dic1 = {'ramya':27,'kavita':31,31:'ami','profusion':'abandent'}
print(dic1[31])
print(dic1.keys()) #print all the keys
print(dic1.values())# print all the values
print(dic1.items()) # print all the key values