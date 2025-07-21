# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 06:13:14 2021

@author: SKOTIYAL
"""


#Unpacking a Sequence into Separate Variables,  N-element tuple or sequence that you would like to unpack into a collection of N variables


p= (4,5)

x,y= p

print(x,y)

#You need to unpack N elements from an iterable, but the iterable may be longer than N elements,
# causing a "too many values to unpack" exception.

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record

print(name)
print(email)
print(phone_numbers)

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)
print(current)


records = [
     ('foo', 1, 2),
     ('bar', 'hello'),
     ('foo', 3, 4),
]

#accessing seq of tagged tuple
def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
        
#for string processing
        
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')

print(uname)
print(homedir)
print(sh)
print(line.split(':')[0])

"""
Sometimes you might want to unpack values and throw them away.
You can’t just specify a bare * when unpacking,
but you could use a common throwaway variable name,
such as _ or ign (ignored). 
"""

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record

print(name)
print(year)