# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 19:11:45 2021

@author: SKOTIYAL
"""


import copy

l=[1,2,3,4]
l1=l

l1[0]='a'

print(l1,id(l1))
print(l,id(l))
print('='*10)


# here new list is not a copy is reference to origanal object,
# change in new object cause change in original object 

mylist = [[1,2],[1,2,3],23,4]

newlist1 = copy.copy(mylist)    #shallow copy

#shallow copy : creates a copy of object but store reference to each element of obj
newlist1[0][1] ="a"
print(mylist,id(mylist))
print(newlist1, id(newlist1))
print('='*10)

newlist1[0]="b"
print(mylist,id(mylist))
print(newlist1, id(newlist1))
print('='*10)

newlist2 =copy.deepcopy(mylist)
#deep copy: creates a copy of object and elements of object
newlist2[1][1] ="a"
print(mylist, id(mylist))
print(newlist2,id(newlist2))



