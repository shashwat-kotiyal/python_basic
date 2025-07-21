# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 17:27:42 2021

@author: skotiyal
"""


import subprocess

res = subprocess.Popen("ls -l",shell=True,stdout=subprocess.PIPE)

out =res.stdout.readlines()

print(out)

from multiprocessing import Pool

def f(x):
    return x*x

from multiprocessing import Process, Queue

def f1(q):
    q.put([42,None,"hello"])
    

if ( __name__ =="__main__"):
    p=Pool(5)
    print(p.map(f,[1,2,3]))
    
    q= Queue()
    p = Process(target =f,args=(q,))
    p.start()
    print(q.get())
    p.join()
    


#asynci0,
#rabbitMQ
#AWS lambda
