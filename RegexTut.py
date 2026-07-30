# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 00:20:43 2021

@author: SKOTIYAL
"""

"""
findall, search, spilt, sub, finditer
meta character:
   [] . ^ $ * + {} | ()
. any single character expect \n 
+ one or more
'\d' matches digit (0 9)
'\D' not a digit  (0 9)
'\w' any word characchter (a-z,A-Z,0-9,_)
'\W' not a wrd character
'\s' whitespace(space tab newline \n,\t)
'\S' not a whitespace
aunker
'\b'

startsWith endWith zeroOrMore oneOrMore specifiedNoOcc eiterOr captureGroup 

Special sequences:

Quantifiers
* zero or more
+ one or more
? 0 or One
{3}
{3-4}range of nos (min, max)
"""

import re

text_to_search = """

abcdefgghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa
Meta characters (Need to be eascaped):
? [] . ^ $ * + {} | () \

shashwat.com

452010
321-555-4321
321--555-4321
123.555.1234
800-555-4321
900-555-4321

Mr. Shashwat
Mr Smith
Ms pran
Mrs. kriti
Mr.T

cat
mat
pat
bat
"""


def eg2():
    return re.compile(r".")


def eg4():
    return re.compile(r"\s")


def eg5():
    return re.compile(r"\S")


def eg6():
    return re.compile(r"\bHa")


def eg7():
    return re.compile(r"\bHa")


def eg7():
    return re.compile(r"\BHa")


def eg7():
    return re.compile(r"\BHa")


def eg8():
    return re.compile(r"^Start")


def eg9():
    return re.compile(r"a$")


def eg10():
    return re.compile(r"\d\d\d.\d\d\d.\d\d\d\d")


def eg11():
    return re.compile(r"\d\d\d[-.]\d\d\d[-.]\d\d\d\d")


def eg12():
    return re.compile(r"[89]00[-.]\d\d\d[-.]\d\d\d\d")


def eg13():
    return re.compile(r"[a-zA-Z]")


def eg14():
    return re.compile(r"[^a-zA-Z]")


def eg15():
    return re.compile(r"[^b]at")


def eg16():
    return re.compile(r"[^a-zA-Z]")


def eg17():
    # \d\d\d.\d\d\d.\d\d\d\d
    return re.compile(r"\d{3}.\d{3}.\d{4}")


def eg18():
    # read Mr  or Mr.
    # re.compile(r'Mr\.')
    # re.compile(r'Mr\.?\s[A-Z]\w+')
    # re.compile(r'M(r|s|rs|)\.?\s[A-Z]\w*')
    return re.compile(r"Mr\.?\s[A-Z]\w*")


def email_match():
    emails = """
    shashwatkotiyal@outlook.com
    shashwat-Kotiyal@university.edu
    abc-321@my-work.net
    """
    pattern = re.compile(r"[a-zA-Z0-9.-]+@[a-zA-Z.-]+\.(com|edu|net)")

    matches = pattern.finditer(emails)
    for match in matches:
        print(match)


def url_match():
    urls = """
    https://www.google.com
    http://shashwatkotiyal.com
    https://nasa.gov
    https://www.youtube.com
    """
    # pat= re.compile(r"https?://(www.)?[a-zA-Z.]+\.(com|gov|nasa)")
    pat = re.compile(r"https?://(www.)?(\w+)(\.\w+)")

    matches = pat.finditer(urls)
    for match in matches:
        print(match)
        print(match.group(0))
        print(match.group(1))
        print(match.group(2))
        print(match.group(3))

    subbed_urls = pat.sub(r"\2\3", urls)  # used back references
    print(subbed_urls)


def gredy_nongredy():
    text = "Hello <tag>inside</tag> world"
    match = re.search(r"<.*>", text)
    print(match.group())

    match1 = re.search(r"<.*?>", text)
    print(match1.group())


def lookahed_lookback() -> None:
    text = "Python 3.10, Python 2.7, Java 1.8"

    # Positive Lookahead	X(?=Y)	Match X only if followed by Y
    # Negative Lookahead	X(?!Y)	Match X only if not followed by Y
    # Positive Lookbehind	(?<=Y)X	Match X only if preceded by Y
    # Negative Lookbehind	(?<!Y)X	Match X only if not preceded by Y

    result = re.findall(
        r"(?<=\.)\d+", text
    )  # look behind positive assertion -> we want all nos before
    print(result)

    s = "$199 299  299$"
    pat = re.compile(r"(?<=\$)\d+")

    result = pat.findall(s)
    print(result)

    pat = re.compile(r"(?=\$)\d+")
    result = pat.findall(s)
    print(result)


def remove_comments():
    s = "875-345-5678    #comment sss"
    # pat=re.compile(r'#.*$')
    # re_obj = re.sub(r'#.*$','',s)
    # print(re_obj)
    # cleaned = pat.sub('\1',s)
    # print(cleaned)

    pat1 = re.compile(r"(\d{3})-(\d{3})-(\d{4})\s*(#.*)")
    match = pat1.findall(s)
    print(match)
    cle = pat1.sub(r"\1\2\3", s)
    print(cle)


def eg1():
    pat = re.compile(r"[0-255][0-255][1-255].[0-255].[0-255].[0-255]")
    pat = re.compile(r"ai{3}")  # if need to find aiii
    pat = re.compile(r"(ai){2}")  # search aiai as capture group is created


# special seq
def eg2():
    pat = re.compile(r"27\b")  # ends with 27
    pat = re.compile(r"\b27")  # starts with 27


# pat = re.compile(r'\d{5}-\d{4}')
# pat = re.compile(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}')

# #valid ip string ((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)

# matchObj = re.match(r'dogs', line, re.M|re.I)

# print("*"*20)
# phrase ="I love open-gaurd,close-gaurd,deepface-gaurd"
#
# match= re.search(r'\w+-gaurd',phrase)
# if match:
#     print(match.group())
#
# match1 = re.findall(r'\w+-gaurd',phrase)
# print(match1)


if __name__ == "__main__":
    # pat = eg11()
    # sentence= 'Start a sentence and then bring to end'
    # matches = pat.finditer(text_to_search)
    # #matches = pat.finditer(sentence)
    # for match in matches:
    #     print(match)
    #     print(match.group())

    # mystr = "this is ip address 10.53.215.53 pin 22209-1234"

    # email_match()

    # url_match()
    # remove_comments()
    # gredy_nongredy()
    lookahed_lookback()

    # pattern = eg10
    # with open('data.txt', 'r', encoding='utf-8' ) as f:
    #     contents = f.read()
    #     matches = pattern.finditer(contents)
    #
    #     for match in matches:
    #         print(match)

    # a raw string tells paython not to handle / in special way.
