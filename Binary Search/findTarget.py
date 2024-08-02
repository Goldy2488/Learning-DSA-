# Binary search 
def binarySearch(arr,target):
    start =0
    end =len(arr)-1
    while start<=end:
        mid = (start+end)//2
        if(arr[mid]>target):
            end=mid-1
        elif arr[mid]<target:
            start=mid+1
        else:
            return mid
    return -1

print(binarySearch([3,4,6,7,9,12,16,17],8))
print(binarySearch([3,4,6,7,9,12,16,17],17))

# Recursive binary search

def recursiveBinarySearch(arr,start,end,target):
    if(start>end):
        return -1
    mid = (start+end)//2
    if(arr[mid]>target):
        return recursiveBinarySearch(arr,start,mid-1,target)
    elif arr[mid]<target:
        return recursiveBinarySearch(arr,mid+1,end,target)
    else:
        return mid
    
arr = [3,4,6,7,9,12,16,17]
print(recursiveBinarySearch(arr,0,len(arr)-1,17))

