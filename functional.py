# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 13:39:48 2021

@author: SKOTIYAL
"""


def smartdiv(div):
    def inner(a,b):
        if (a>b):
            r = div(a,b)
            return r
        if(b>a):
            r =div(b,a)
            return r
    return inner

def div(a,b):
    c = a/b
    return c

div = smartdiv(div)
d = div(5,10)
print(d)

print("*"*20)

from functools import partial

def email(id,domain,extension):
    print(id+domain+extension)

db1 = partial(email,"foziya.com")
#db1("foziya.com")

db1("@gmail",".com")
#print(db1)
print("*"*10+"lazy evaluated function "+"*"*10)
#use to run infinte sequence


def lazy_return_random_attacks():
    """ Yeild attack each time """
    import random
    attacks = {"kimura":"upper body",
               "straight_ankle_lock":"lower body",
               "arm_triangle":"upper body",
               "key_lock":"upper body",
               "knee_bar":"lower body"}

    while True:
        random_attack= random.choices(list(attacks.keys()))
        yield random_attack

attack = lazy_return_random_attacks()
print(attack,type(attack))

print(next(attack))
print(next(attack))
#infinte list of radom choices

print("*"*5+"Decorators function that warp other function "+"*"*5)

def randomized_speed_attack_decorator(function):
    import random
    import time
    def wrapper_func(*args,**kargs):
        sleep_time=random.randint(1, 3)
        print(f"Atticking after {sleep_time}seconds..")
        time.sleep(sleep_time)
        return function(*args,**kargs)        
    return wrapper_func


@randomized_speed_attack_decorator
def lazy_return_random_attacks1():
    """ Yeild attack each time """
    import random
    attacks = {"kimura":"upper body",
               "straight_ankle_lock":"lower body",
               "arm_triangle":"upper body",
               "key_lock":"upper body",
               "knee_bar":"lower body"}

    while True:
        random_attack= random.choices(list(attacks.keys()))
        yield random_attack


for i in range(3):
    print(next(lazy_return_random_attacks1()))
    
    
print("*"*5+"Call class like function -> __call__ "+"*"*5)
    

class AttackFinder():
    """find attack"""
    def __init__(self,attack):
        self.attack=attack
        
    def __call__(self):
        attacks = {"kimura":"upper body",
               "straight_ankle_lock":"lower body",
               "arm_triangle":"upper body",
               "key_lock":"upper body",
               "knee_bar":"lower body"}
    
        if not self.attack in attacks:
            return "unknown location"
        return attacks[self.attack]

attack_finder = AttackFinder("key_lock")
print(attack_finder())      

print("*"*5+"lambda function"+"*"*5)

sqfunction = lambda x: x**2
print(f"squred no: {sqfunction(4)} ")
