

print("#lamda function are anonymous function")
print("#lamda parameters:return value")

x=2
y=3

res_2x =lambda x: 2*x
#print res_2x             `this is wrong we have only declear lambda function it will return <function <lambda> at 0x000000000498CBA8>
print (res_2x(x))          #we should call then only it will return value
res_sum=lambda x,y:x+y
print (res_sum(x,y))

mx= lambda x,y:x if x>y else y   #here x and y is different not 2,3 it depends on what is in call
print (mx(8,6))

#map apply the function in each elements of sequence 
#and return modified sequence
print("# map(function,list)")

n= [5,4,3,2,1]
print(list(map(lambda x:x*x,n)))

#filter item out of sequence and return filter list
print("# filter(condition/function,list)")
print ("filter greater then 3")
#print (filter(lambda x:if x>3,n))
print (list(filter(lambda x:x>3,n)))
#print (filter(if(x>2),n))  wrong way bool object cannot be callable

#reduce function apply to item of seq uses result of first parameter of next operation ,return an item not list
# list  ,[m,n.p] ,f()  reduce---> f(f(m,n),p)
#reduce funtion multiplying all ele of list

import functools
print(functools.reduce(lambda x,y:x*y,n))

#difference
l = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x:x*2,l)))

print(list(filter(lambda x:x*2,l)))

