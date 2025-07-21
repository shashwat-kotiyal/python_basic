# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 23:32:22 2021

@author: SKOTIYAL
"""


class A():
    def classPrint(self):
        print("IN A")
    pass

class B():
    def classPrint(self):
        print("IN b")
    pass
class C(A):
    def classPrint(self):
        print("IN c")
    pass

class D(C,B):
   # def classPrint():
   #     print("IN D")
   pass
        
r= D()
D.classPrint()

print("*"*20)

class Competitor: pass


corner = Competitor()
corner.name="sudheer"
corner.age="27"

print("*"*20)
class JonJones:
    """ @property is shortcut for creating read only method """
    @property
    def reach (self):
        return 84
        
    """ @staticmethod bolts a function in class"""
    @staticmethod
    def reach1():
        return 85;
    

    
jon_jones = JonJones()
print(jon_jones.reach)
print(jon_jones.reach1())
print("*"*20)
"""Meta class, are the class that creates classes"""

class MetaClass(type):pass
class FirstClass(metaclass=MetaClass):pass
print(f"Metaclass is a subclass of type:{issubclass(MetaClass,type)} ")

print("*"*20)
import collections

class OrderAttacks(type):
    @classmethod
    def __prepare__(metaclass,name,bases,**kwds):
        return collections.OrderedDict()
    
    def __new__(cls,name,bases,namespace,**kwds):
        result= type.__new__(cls,name,bases,dict(namespace))
        result.attack_defination_order = list(namespace)[2:]
        return result
    
class Attack(metaclass=OrderAttacks):
    def Armbar(self):pass
    def kimura(self):pass
    def kneebar(self):pass
    def jab(self):pass

attacks= Attack()
print(f"Attack methods were created in this order:\n {attacks.attack_defination_order}")
        
print("*"*20)    

tournaments =["EuropeanChampionship-UEFA",'copaamerica-CONMEBOL',"AfricanCupOfNation-CAF",'AFC','OFC']
import logging
while True:
    try:
        tournament=tournaments.pop()
        print(f"{tournament}")
    except IndexError:
        print("there is no more tournaments")
        logging.exception("Excetion logged: there is no more tournaments")
        break;

