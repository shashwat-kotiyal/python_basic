# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 00:20:43 2021

@author: SKOTIYAL
"""


import re
"""
 findall, search, spilt, sub, finditer
meta character:
   [] . ^ $ * + {} | ()
=  set anychar(expect \) startsWith endWith zeroOrMore oneOrMore specifiedNoOcc eiterOr captureGroup 

Special sequences:

"""

mystr = "this is ip address 10.53.215.53 pin 22209-1234"
pat = re.compile(r'[0-255][0-255][1-255].[0-255].[0-255].[0-255]')
pat = re.compile(r'ai{3}')      #if need to find aiii
pat = re.compile(r'(ai){2}')    #search aiai as capture group is created

#special seq
pat = re.compile(r'27\b') #ends with 27
pat = re.compile(r'\b27') #starts with 27


pat = re.compile(r'\d{5}-\d{4}')
pat = re.compile(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}')
#valid ip string ((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)
matches = pat.finditer(mystr)
for match in matches:
    print(match)
    print(match.group())
    
    
#matchObj = re.match( r'dogs', line, re.M|re.I)
    
print("*"*20)
phrase ="I love open-gaurd,close-gaurd,deepface-gaurd"

match= re.search(r'\w+-gaurd',phrase)
if match:
    print(match.group())
    
match1 = re.findall(r'\w+-gaurd',phrase)
print(match1)
