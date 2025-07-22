
#second largest element in a array




def Largest(arr):
    largest= -1
    secondlargest = -1
    n= len(arr)
    for i in range(0,n,1):
          if arr[i]>largest:
              largest= arr[i]
    print (largest)
    return largest

def secondLargest(arr):
    largest= -1
    secondlargest = -1
    n= len(arr)
    for i in range(0,n,1):
          if arr[i]>largest:
              largest= arr[i]
    print (largest)
    return largest

if __name__ == "__main__":
    arr= [1,4,3,7,7,6]
   #sort_list=sorted(list) return sorted list without modifying orignal list
   # sort_arr=sorted(arr)

    # list.sort() is inplace does not return any value
    arr.sort()
    print(arr[1])