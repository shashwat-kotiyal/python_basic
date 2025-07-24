


#removing spaces from string, lstrip(), 

name  = '   shashwat   kotiyal  '

print(name.lstrip()) #removing spaces from start
print(name.rstrip()) #removing spaces from end
print(name.strip())  #removing spaces from start and end

#replace, find ,

print(name.replace('kotiyal','narayan'))

# how many time s is coming in string

x = len(name)
y = len(name.replace('s',''))
print("no of s:",x-y)

#find
str1 ='sh'
str2 ='ko'
print("give first occurance of sh: {}".format(name.find(str1))) #give the first occurance
print(f"give first occurance of ko: {name.find(str2)}")

#split : will split data and store in from of list

name1 = name.split(" ")
print(name1)

#convert string to list
str= "clangour"
print(list(str))
#print(str.split(''))


#You need to split a string into fields, but the delimiters (and spacing around them) aren’t consistent throughout the string.

line = 'asdf fjdk; afed, fjek,asdf,      foo'

import re

print(re.split(r'[;,\s]\s*',line))

#If you don’t want the separator characters in the result,
# but still need to use parentheses to group parts of the regular expression pattern, 
#make sure you use a noncapture group, specified as (?:…​).
#re.split(r'(?:,|;|\s)\s*', line)
fields = re.split(r'(?:,|;|\s)\s*',line)


import os

filenames = os.listdir('.')

pyfiles = [name for name in filenames if name.endswith(".py")]

print(any(name.endswith('.py') for name in filenames))
# - any(...) returns True if at least one item in the generator is True



#import 
