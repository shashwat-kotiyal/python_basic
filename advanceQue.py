import re
from re import finditer

def stringMultipy():
    s= 'alpha2gamma10beta0'
    pat=re.compile(r'([a-zA-Z]+)(\d+)')  #\w any word characchter (a-z,A-Z,0-9,_)

    matches =pat.finditer(s)

    for match in matches:
        #print(match)
        print(match.group(1) * int(match.group(2)))
        #print(match.group(2))

    matches1 = pat.findall(s)
    for sub_string,no in matches1:
        print(sub_string * int(no),end='')
    print()


def findIP():
    s= 'my ip is  10.32.114.14'
    #pat = re.compile(r'(^[1-255]\.[0-255]\.[0-255]\.[1-255])')  # wrong pattern  [1-255] doesn't mean "number from 1 to 255" — it's just a character set
    #pat = re.compile(r'(\d{1-3}\.\d{1-3}\.\d{1-3}\.\d{1-3})')
    pat = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    matches =pat.finditer(s)
    for match in matches:
        print(match)
        print(match.group(1))

def strongPasswordvalidator()->None:
    s="Asfe4egrf009r@"
    pat=re.compile(r'(?=.{8,})(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).*')
    matches = pat.findall(s)
    for match in matches:
        print(match)

def extractFunctionName(filename: str)->None :
    #s= "def addf():"
    #pat=re.compile(r'^def\s(\w+)\(\w+\):$') wrong
    pat = re.compile(r'def\s+(\w+)\(.*?\).*?:')    #\(.*?\) – non-greedy match of anything inside parentheses (arguments)
    #matches = pat.finditer(contents)

    with open(filename,'r') as file:
        contents =file.read()
        matches = pat.finditer(contents)
        for match in matches:
            #print(match)
            print(match.group(1))

    #memomry
    # with open(filename,'r') as file:
    #     for line in file:
    #         matches = pat.finditer(line)
    #         for match in matches:
    #             if match:
    #                 print(match.group(1))




def duplicate_words()->None:
    s= 'this is the cat the'
    text = "the the cat and and the dog"
    s1 = "this is is a test test sentence"

    pat =re.compile(r'\b(\w+)\s*\1\b',flags=re.IGNORECASE)
    matches =pat.findall(text)
    print(matches)

    clean = pat.sub(r'\1',text)
    print(clean)

    # matches = pat.finditer(s)
    # for match in matches:
    #     print(match)
        #print(match.group(1))
    #pat1 = re.compile(r'\b(\w+)\s+\1\b')
    #cleaned =pat.sub(text)

def remove_all_dups():
    text = "the the cat and and the dog"
    text_list = text.split()
    print(text_list)
    my_set=set()        #define set
    for words in text_list:
        words =words.lower()
        if words not in my_set:
            my_set.add(words)
    print(my_set)


def is_valid_anagram(s1: str,s2: str)->bool:
    if len(s1) != len(s2):
       print('not a anagram')
       return False
    char_list_s1 ={}
    char_list_s2 ={}

    for ch in s1:
        if ch in char_list_s1 :
            char_list_s1[ch] +=1
        else:
            char_list_s1[ch] =1

    for ch in s2:
        if ch in char_list_s2 :
            char_list_s2[ch] += 1
        else:
            char_list_s2[ch] = 1

    print(char_list_s1)
    print(char_list_s2)

    for key in char_list_s1:
        if key not in char_list_s1 or char_list_s1 != char_list_s2:
            print("not a anagram")
            return False
    return True


def is_valid_anagram1(s1: str,s2: str)->bool:
    from collections import Counter
    if len(s1) != len(s2):
        return False
    print(Counter(s1))
    print(Counter(s2))
    return Counter(s1) == Counter(s2)

def is_valid_anagram2(s1: str,s2: str)->bool:
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)  #O(nlogn)



def first_and_last(arr: list,target: int) -> list:
    n= len(arr)
    start, end  = -1, -1
    for i in range(n):
        if arr[i] == target:
            start = i
            break
    # for i in range(start,n):
    #     if arr[i] == target :
    #         end = i
    for i in range(n-1,start,-1):
        if arr[i] == target:
            end = i
            break
    return [start,end]


def first_and_last1(arr,target):
    start = first(arr, target)
    print(start)
    end = last(arr, target)
    return [start,end]

def first(arr, target):
    left, right = 0 , len(arr)-1
    if arr[0] == target:
        return 0
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target and arr[mid -1] < target:
            return mid
        elif arr[mid] < target:     # still before start pos
            left = mid+1
        else:
            right = mid-1
    return -1

def last(arr, target):
    left, right = 0, len(arr) - 1
    if arr[-1] == target:
        return len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target and arr[mid + 1] > target:
            return mid
        elif arr[mid] > target:
            right = mid-1
        else:
            left = mid+1
    return -1


def kth_largest(arr,k):
    sorted(arr)       #O(nlogn)
    return arr[len(arr)-k]

def kth_largest1(arr,k):
    import heapq
    arr =[-elem for elem in arr]   # top find smallest element not greatest
    print(arr)
    heapq.heapify(arr)    # make respect heap properity
    for i in range(k-1):   #extract k-1 times
        heapq.heappop(arr)
    return -heapq.heappon(arr) #one more extract and rverser sign , O(n+klog n), k llr to n O(n+klogn) = O(nlogn)


"""
Write a regex to validate a strong password (min 8 chars, 1 uppercase, 1 digit, 1 special char).

Extract function names from a Python script using regex.

Use a regex to find duplicate words in a sentence (e.g., "the the cat").

Explain the difference between:

Lookahead vs Lookbehind assertions

With examples: (?=...), (?!...), (?<=...), (?<!...)

Can regex be used to parse HTML or JSON? Why or why not?
"""
if __name__ =='__main__':

    stringMultipy()

    #findIP()
    #strongPasswordvalidator()
    #extractFunctionName("RegexTut.py")
    #duplicate_words()
    #remove_all_dups()

    #print(is_valid_anagram('abbc','bbac'))
    #print(is_valid_anagram1('abbc', 'bbac'))
    #print(is_valid_anagram2('salesman', 'nameless'))

    #   given a sorted array of int arr and an integer target
    #     find the index of first and last position of target in arr
    #     if target not found return [-1,-1]
    #  a = [2,4,5,5,5,5,5,7,9] ,t= 5, o/p=[2,6]
    #print(first_and_last([2,4,5,5,5,5,6,7,9,5],5))
    # if array is sorted than can use binary search
    # print(first_and_last1([2, 4, 5, 5, 5, 5, 6, 7, 9], 5))
    # print(first_and_last1([2,2], 2))
    # print(first_and_last1([2], 2))

    #print(kth_largest([2, 4, 5, 5, 5, 5, 6, 7, 9],3))

    #find symmetric tree

    #genrate paranthess
    # import os
    #
    # abs_path = os.path.abspath(__file__)
    # print(abs_path)
    s = 'sddsdgfdhfhfgrt'
    dict = {}
    for ch in s:
        if ch in dict:
            dict[ch] +=1
        else:
            dict[ch] = 1
    print(dict)



