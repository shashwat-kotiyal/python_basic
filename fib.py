
def fib(n):
    if (n<=1):
        return n
    else:
        return (fib(n-1)+fib(n-2))

n = int(input("enter the no of terms:\t"))
if n<=0:
    print ("Enter positive integer")
else:
    print("fibonacci sequence")
    for i in range(n):
        print (fib(i))