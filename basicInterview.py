import os, glob

def getChildpy():
    os.chdir("C:\\Users\\Saransh\\PycharmProjects\\Algo\\array")
    for file in glob.glob("*.py"):
        print(file)

#comman interview questions
#Fizz buzz

def fizzBuzz():
    for num in range(1,101):
        if num% 5 == 0 and num %3==0:
            print("FizzBuzz")
        elif num%3 ==0:
            print ("Fiz")
        elif num %5== 0:
            print ("Buzz")
        else:
            print(num)

#fibnocii
def fib(n):
    if n<=1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fibIt(n):
    a,b =0,1
    for i in range(0,10):
        print(a,end='')
        a,b=b, a+b

def fibgen(num):
    a,b =0,1
    for i in range (0,num):
        yield f"{i+1}:{a}"
        a, b= b,a+b


if __name__ =='__main__':

    x=10
    y=10
    z=10
    print(id(x),id(y),id(z))

    a=10000000000
    b=10000000000
    print(id(a),id(b))

    print(-10//3)  # output is -4 instead of -3.3
    print(2**3**2)  #some operator prefer rt to left ans is  2**9 = 512 not 64
    print(8//4//2)  # precedence lt -> rt applied , associativity from rt to left

    name= "shantanu"
    print(name[2:8:-2]) #nohing will be in o/p as will not find end index in going opposite direction
    print(name[2:8:-2])

    a=[1,2,3]
    b=[4,5,6]
    c=[7,8,9]
    print(a+b+c)
    print(list(zip(a,b,c)))
    l=[]
    l.append(a)
    l.append(b)
    l.append(c)
    print(l)
    print(a.extend(b))



    s= 'aabaaabbbbcc'
    freq={}
    for char in s:
        if char not in freq:
            freq[char]=1
        else:
            freq[char]+=1
    print(freq)
# 1 write in white paper
# 2 basic control flow
        # if ,else, for while

#3 be able to discuss how you've use python
        # web srapping -> pull weather info ,  sys tem program
        # prg to find file in copy

    print("fib")
    for i in range(5):
        print(fib(i),end='')
    print()
    fibIt(5)

#5 basic python data type and how to itrate
    #how this datatypes work eg: dict == hash table
    #adv and weekness
    #when to use each data type
    #list
    my_list = [1,2,3,4,5,6,7,8,9,10]
    # for ele in my_list:
    #     print(ele)

    #tuple
    my_tuples =(1,2,3,4,5,6,7,8,9)
    # for i in my_tuples:
    #     print (i)

    #dict
    my_dict = {'name': 'bruno', 'age':2, 'occupation': 'RAN ENGINEER' }
    #python3 iteritems is remove and item is used
    for key, value in my_dict.items():
        print("My {} is {}".format(key,value))


    #set
    my_ser={10,20,30,40,50}

#6 use list, dict  comprehension ,
    my_list= [1,2,3,4,5]
    squares_list = [x*x for x in my_list]

#7 how to use Genrators
    #genrator function eg: xrange,  my_dict.iteritems= give one item at a time
    # for items in fibgen(10):
    #     print(items)

#8 knows basic of oops
#   write sample file and program write them over and over again from scratch ,
    #how to
    #self, instance of class , inherit from class , initial class , over ride methods,

#9 Have python related questions ready to ask interviewer
#   eg: are you using python2 and python3 , why diff , eg
#   eg: what databases they are using
#    eg: what test modules they are using unit testing

#10 Know basic of other technology
#   eg: sql, bash scripting  , T shape skill set -> know basic of everything what they are lsited in job profile.