


def square(nos):
    result =[]
    for i in nos:
        result.append(i*i)
    return result
#same can be done using genrators

def square_numbers(nums):
    for i in nums:
        yield (i*i)

my_nos= square([1,2,3,4,5])
my_nums= square_numbers([1,2,3,4,5])    #will return genrator object to access we need to use next method
                                        #generator does not hold the entire result it will yeild one result at a time

print (my_nums)
#print next(my_nums)
for num in my_nums:
    print (num)

# can easily done by list comprehension
my_sq= [x*x for x in [1,2,3,4]]
my_sq_nums = (x*x for x in [1,2,3,4])   # returns a genrator which is better in performance 