
def comman(l1,l2):
    set_l1= set(l1)
    set_l2= set(l2)
    #print (set_l1)                 #set arrange in order and eleminate duplicate elements
    if (set_l1 & set_l2):
        print (set_l1 & set_l2)
    else:
        print ("no comman element")
    return




l1=[1,2,3,4,5,6,1]
l2=[6,7,8,9,10]
comman(l1,l2)