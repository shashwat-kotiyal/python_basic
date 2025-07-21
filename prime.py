# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 08:45:44 2021

@author: SKOTIYAL
"""
#An efficient solution is to use Sieve of Eratosthenes to find all prime numbers from till n

def sumOfPrimes(n):
    prime =[True]*(n+1)   #making list of n+1 elements

    p=2
    while(p*p <=n):
        if(prime[p]== True):
            i= p*2
            while i<=n:
                prime[i]= False
                i+=p
        p+=1
    sum =0
    for i in range(2,n+1):
        if(prime[i]):
            print(i)
            sum+=i
    return sum

n = 11    #2+3+5+7+11
print("sum:",sumOfPrimes(n))

'''    
    for(p=2;p*p<=n;p+=1){
    if(prime[p]== true)
        for(i=i*2;i<=n;i+=p)
            prime[i]=false
    sum=0
    for (i=2;i<n;i++){
        if(prime[i])
            sum =sum+i
            }
    
    }
'''      