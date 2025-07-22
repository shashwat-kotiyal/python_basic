#kadane's algo



def sumOfSubArray( arr):
    INT_MAX= -2**31
    n = len(arr)
    for i in range(0, n, 1):
        for j in range (1, n, 1):
            sum=0



def loop1():
    for i in range(0,3,1):
        print (f'i:{i}')
        for j in range(0,3,1):
            print(f'j:{j}',end=" ")
        print()

def loop2():
    for i in range(0,3,1):
        print (f'i:{i}')
        for j in range(0,3,1):
            print(f'j:{j}',end="")
            for k in range(i, j, 1):
                print(f'k:{k}',end="")
            print()

