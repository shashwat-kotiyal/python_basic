
nums =[1,2,3,4]
print("#if Something(Object) is iteratable must implement __iter__ and __next__")
print("#dir(): return all the properties and method of the object")
print ("nums:",dir(nums))

print("# get an iterator using iter()")
#print (next (nums)) list operator is not a iterator
#i_nums = nums.__iter__() same as below
i_nums = iter(nums)
print ("\ninums:",dir(i_nums))

"""
while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break
"""


class MyRange:
    def __init__(self,start,end):
        self.value =start
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value>= self.end:
            raise StopIteration
        current = self.value
        self.value +=1
        return current

num = MyRange(1, 10)
print("# pratical example is to make class iteratable")
print(next(num))
print(next(num))


def my_range(start):
    current =start
    while True:
        yield current
        current+=1

nums=my_range(1)
print("#generators used to createing extremly useful easy to read iterators ,")
print("# look like normal functions but instead of return they yeid the value, keep this value and use agian")
for nu in num:
    print(nu)