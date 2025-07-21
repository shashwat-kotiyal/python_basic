


def convertOpposite(str):
    ln= len(str)
    for i in range(ln):
        if (str[i] >='a' and str[i]<='z'):        #return an integer representing the Unicode code point of the character eg: a =97
            # str[i] = str[i] - 32
            #str[i] = str(ord(str[i]) - 32)
            str[i] = chr(ord(str[i])-32)
        elif (str[i]>='A' and str[i]<='Z'):
            str[i] = chr(ord(str[i])+32)
    return


str = 'shashWAT'
str = list(str)       #conversion of str to slist is important as str object will not support assignment
convertOpposite(str)
str=" ".join(str)
print(str)