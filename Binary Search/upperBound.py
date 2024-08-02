# find the upper bound 

# def upperBound(arr,target):
#     start = 0
#     end = len(arr)-1
#     ans =0
#     while start<=end:
#         mid = (start+(start+end)//2)//2 # for handle the overflow you can also use (start+end)//2 in python
#         print(start,end,mid)
#         if(arr[mid]<=target):
#             start = mid+1
#             ans = mid
#         else:
#             end=mid-1
#     return ans

# arr = [2,3,6,7,8,8,11,11,11,12,16]
# target = 11
# print(upperBound(arr,target))


# recursive binary search
def recursiveUpperbound(arr, start, end, target):
    if start > end:
        return start  # When target is not found, return the insertion point
    
    mid = (start + end) // 2
    print(start, end, mid)
    
    if arr[mid] <= target:
        return recursiveUpperbound(arr, mid + 1, end, target)
    else:
        return recursiveUpperbound(arr, start, mid - 1, target)

arr = [1, 2, 3, 3, 7, 9, 9, 9, 11]
print(recursiveUpperbound(arr, 0, len(arr) - 1, 9))  # Output should be 9