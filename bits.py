# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 09:21:39 2021

@author: SKOTIYAL
"""
#bit shift >>
#bit anding :masking ->checking on or off
#bit oring :mearging ->changing bit on
#QUE1:Count number of bits to be flipped to convert A to B

def fun_xor(a,b):
    return (a^b)


def countbit(n):
    count=0
    while(n):
        count += 1
        n &=(n-1)
    return count
        
def countbitShift(n):
    count = 0
    while(n):
        count += n&1
        n >>= 1
    return count
    
    
n = fun_xor(10,20)

print("xor:",n)
print(countbit(n))
print(countbitShift(n))

#python objects (booleans, integers, floats, strings, and tuples) are immutable -> call by value
#list,dictonary = mutable -> call by reference 


#QUE2: Swap two nibbles in a byte

def swapNibble(x):
    return ((x & 0x0F)<<4 |(x & 0xF0)>>4)

x= 100
print("x:",x)
print("swapNibble:",swapNibble(x))
