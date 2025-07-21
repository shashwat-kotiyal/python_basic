# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 23:27:51 2021

@author: SKOTIYAL
"""
# Python generators are a simple way of creating iterators.
# A generator is a function that returns an object (iterator) which we can iterate over (one value at a time).

# A decorator takes in a function, adds some functionality and returns it
# This is also called metaprogramming because a part of the program tries to modify another part of the program at compile time.

def function1(msg):
    print (msg)

function2 = function1
#everything is object in python,a function can assign to another
function2("shashwat")

#A function can pass another function as argument (map, filter, reduce)

def operater(func,x):
    result =func(x)
    return result

def inc(x):
    return(x+1)

def dec(x):
    return(x-1)


print(operater(inc,3))















def div(a,b):
    print(a/b)




def smart_div(func):
    
    def  inner(a,b):
        if a<b:
            a,b =b,a
        return func(a,b)
    return inner

div = smart_div(div)
div(2,4)


#creating new function taking function as a parameter, 
#change behivour of funtion at compile time