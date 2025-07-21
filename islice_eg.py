

from itertools import islice
from itertools import count
import time


def counting_from_no():
    for i in x:
        print (i)
        time.sleep(1)
    return

def counting_to_zero():
    print("##only first 10 values")
    for i in islice(count(10,-1),10):              
        print (i)
    
    print("##start, end, step 5th to 10th ele of iterator")
    for i in islice(count(10,-1),5,10):           
        print (i)
        
    print("##start, end, step 5th to 10th ele of iterator with step")    
    for i in islice(count(10,-1),5,10,2):
        print (i)
    return

x= count(10,1)  #count is the infinate iterator   count( start,step)
                #islice allows to slice the iterator


def islice_range():
    for i in islice(range(10),5):
        print (i)

counting_to_zero()
