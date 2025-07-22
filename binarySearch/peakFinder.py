#peak finder



"""
6/2=3
5/2=2

class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {

        int hi= arr.size()-1;
        int lo= 0;

        while(hi>lo){
           long int mid=lo+(hi-lo)/2;

         if(arr[mid+1]>arr[mid])
             lo= mid+1;
         else
             hi=mid;
        }
        return lo;
    }
};

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int lo=0;
        int hi=nums.size()-1;

        while (lo<hi){
        int mid= lo + (hi-lo+1)/2;

            if(nums[mid]<= target)
                lo = mid;
            else
                hi = mid-1;

        }
        if (nums[lo]==target){
            return lo;
        }
        else
            return -1;
 """

def peakFinderB(arr: [int])->int:
    n= len(arr)
    for  i in range(n):
        if (i==0 or arr[i-1]<arr[i]) and ( i==n-1 or arr[i]>arr[i+1]):
            return i
    return -1

def peakFinder1(arr:[int])-> int:
    n = len(arr)
    if n==1:
        return 0
    if arr[0] > arr[1]:
        return 0
    if arr[n-1] > arr[n-2]:
        return n-1
    low=1
    high=n-2

    while low <= high:
        mid= low + (high-low)//2
        if arr[mid] > arr[mid-1] and arr[mid]> arr[mid+1]:
            return mid
        elif arr[mid] > arr[mid -1]:
            low= mid+1
        else:
            high=mid-1
    return -1


# def sortedRotatedArray(a):
#     n=len(a)
#     low = 0
#     high = n-1
#     import sys
#     ans = sys.maxsize
#     while low >= high:
#         mid= (low+high)//2
#         if a[low]>a[mid]:






if __name__== "__main__":
###########################################################################
    # arr = [1, 5, 8, 10, 15, 3, 4]
    # idx = peakFinderB(arr)
    # print(f"Peak found at index {idx} with value {arr[idx]}")
    #
    # arr1 = [1, 3, 20, 4, 1, 0]
    # idx1 = peakFinderB(arr1)
    # print(f"Peak found at index {idx1} with value {arr1[idx1]}")
    #
    # arr2 = [2,3]
    # idx2 = peakFinderB(arr2)
    # print(f"Peak found at index {idx2} with value {arr2[idx2]}")
    #
    # arr3 = [8]
    # idx3 = peakFinderB(arr3)
    # print(f"Peak found at index {idx3} with value {arr3[idx3]}")
##################################################################

    arr = [4, 5, 6, 7, 0, 1, 2, 3]
   # print(sortedRotatedArray(arr))