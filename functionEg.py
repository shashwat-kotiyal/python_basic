# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 23:06:34 2021

@author: SKOTIYAL
"""
#Que1:You want to write a function that accepts any number of input arguments.

def avg(first, *rest):
    return ((first + sum(rest))/ (1+len(rest)))

print(avg(1,2))


def anyargs(*args, **kwargs):
    print(args)      # A tuple, positional
    print(kwargs)    # A dict, keyword argument 
    
#Que2: Writing Functions That Only Accept Keyword Arguments

def recv(maxsize,*,block):
    print("recived arguments")
    pass

#recv(1024,True)   #err
recv(1024,block=True)

def minimum(*values,clip=None):
    m = min(values)
    print(m)
    if clip is not None:
        m = clip if m< clip else m
    return m

print(minimum(1, 5, 2, -5, 10))          # Returns -5
print(minimum(1, 5, 2, -5, 10, clip=0))  # Returns 0

#que3: function annotation

def add(x:int, y:int) -> int:
    return x + y

print(add.__annotations__)

#que3: Returning Multiple Values from a Function untuple
    
    
def myfunc():
    return 1,2,3

a,b,c = myfunc()

print(a,b,c)

d = 1 , 2
print(d,"::",type(d))

#Que4: Defining Functions with Default Arguments

#Que5: INline function

add = lambda x,y:x+y

print(add(3,4))

#sort names by surnames
names =["anindo das",'rahul singh','kavita mishra','patra']

print(sorted(names,key=lambda x:x.split()[-1].lower()))

#que 9: closer, function are obj,A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.
#   execute inner function outside its scope
#You would like to extend a closure with functions that allow the inner variables to be accessed and modified.
def outer():
    n=0
    def inner():          # Closure function
        print("n=",n)
    def get_n():
        return n
    def set_n(value):
        nonlocal n  #nonlocal declarations make it possible to write functions that change inner variables
        n = value
        #Attach as function attributes as function is obj
    inner.get_n=get_n
    inner.set_n=set_n
    
    return inner

f = outer()
print(f())
f.set_n(10)
print(f())
f.get_n()

#A slight extension to this recipe can be made to have closures emulate instances of a class.
import sys
class ClosureInstance(object):
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals
        # Update instance dictionary with callables
        self.__dict__.update((key,value) for key, value in locals.items()
                             if callable(value) )
    # Redirect special methods
    def __len__(self):
        return self.__dict__['__len__']()

# Example use
def Stack():
    items = []
    def push(item):
        items.append(item)
    def pop():
        return items.pop()
    def __len__():
        return len(items)
    return ClosureInstance()

s = Stack()
print(s)
s.push(10)
s.push(20)
s.push('Hello')
print(len(s))
s.pop()
s.pop()
s.pop()
    
