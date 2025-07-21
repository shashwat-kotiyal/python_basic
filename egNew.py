# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 05:28:36 2020

@author: SKOTIYAL

Whenever a class is instantiated __new__ and __init__ methods are called. 
__new__ method will be called when an object is created 
and __init__ method will be called to initialize the object
"""


class A(object): 
    def __new__(cls): 
         print("Creating instance or object") 
         return super(A, cls).__new__(cls)    #for calling init

    def __init__(self): 
        print("Init is called")
        
"""
Instance can be created inside __new__ method 
either by using super function or 
by directly calling __new__ method over object, where if parent class is object. 
That is instance = super(MyClass, cls).__new__(cls, *args, **kwargs) 
or instance = object.__new__(cls, *args, **kwargs)
"""  
  
A()
#when print obj will get <__main__.A at 0x1d0XXXXXXX>
#get around this by defining a __str__ or __repr__ function 
#to display the data for the instance in a custom way
print("\n \tMyClass eg:  ")
class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

    
    
obj = MyClass()
print(obj.method())    
#take parameter self which point to instance of myclass when method is called
#Through the self parameter, instance methods can freely access attributes and other methods on the same object. 
#This gives them a lot of power when it comes to modifying an object’s state.
#Not only can they modify object state, instance methods can also access the class itself through the self.__class__ attribute. This means instance methods can also modify class state.        

print(obj.classmethod())
#Instead of accepting a self parameter, class methods take a cls parameter that points to the class—and not the object instance—when the method is called.
#Because the class method only has access to this cls argument,it can’t modify object instance state. 
#That would require access to self.However, class methods can still modify class state that applies across all instances of the class.

print(obj.staticmethod())
#This type of method takes neither a self nor a cls parameter (but of course it’s free to accept an arbitrary number of other parameters).
#Therefore a static method can neither modify object state nor class state. Static methods are restricted in what data they can access - and they’re primarily a way to namespace your methods. 'static method called'
    

print( MyClass.classmethod())
print( MyClass.staticmethod())

#print( MyClass.method())
#TypeError: method() missing 1 required positional argument: 'self'
#And this is to be expected — this time we didn’t create an object instance and tried calling an instance function directly on the class blueprint itself. This means there is no way for Python to populate the self argument and therefore the call fails.
    

#maybe you dont want to change the code of existing function
#Que:  if b>a then divide b/a change values without touching function
#using decorator we can add extra features in existing functions
 
print("\n\tSmart div eg")
def div(a,b):
    print(a/b)
    
def smart_div(func):          #fnction pass as arg
    
    def inner(a,b):
        if(a<b):
            a,b=b,a
        return(func(a,b))       #function got decorated, inner() function inside the decorator is the same as the parameters of functions it decorates 

    return inner                #function returning a function

div =smart_div(div)    #assignment step
div(2,4)

"""
A function can pass as arg
A method can return function

decorator : do meta programming, as on compile time we are modifing behivour of other part of program 
https://www.programiz.com/python-programming/decorator
"""


print("\n\tStudent eg")

class student():
   counter =0    
   clg_name="xyz"          #class variable
   def __init__(self,name,age,marks):
        self.name =name
        self.age =age
        self.marks=marks
        student.counter = student.counter+1
   
   def msg(self):
       print(self.name+" "+self.age)
       
   @classmethod
   def object_count(cls):
       return cls.counter
   @classmethod
   def get_per(cls,name,marks):
       return cls(name,str(int(marks))/600 *100)
   @staticmethod
   def get_age(age):
       if (age<17):
           print("belong to school")
       else:
           print("doesnt belong to school")
               
               
s1 =student('nia',20,75)
s2 =student('ria',20,85)
print(s1.name, s1.age)

print(student.clg_name)
#can be access by all the object of class or class,owned by class itself,shared by all the object of class
#
print (student.object_count())
print (s1.object_count())


#


#class Employee:
 #   def 

