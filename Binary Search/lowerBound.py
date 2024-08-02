# You are given an array 'arr' sorted in non-decreasing order and a number 'x'. You must return the index of the lower bound of 'x'.

arr = [1,2,3,3,7,9,9,9,11]
ans = len(arr)
def lowerbound(arr,target):
    start = 0
    end = len(arr)
    ans = 0
    while start<= end:
        mid = (start+(start+end)//2)//2
        if(arr[mid]>=target):
            end = mid-1
            ans = mid
        else:
            start= mid+1
    return ans

print(lowerbound(arr,1))
print(lowerbound(arr,9))


# by RecursiveBinarySearch

# arr = [1,2,3,3,7,9,9,9,11]
# ans = len(arr)
# def recursivelowerbound(arr,start,end,target,ans):
#     print(arr,start,end,target,ans)
#     if start>end:
#         return ans
#     mid = (start+(start+end)//2)//2
#     if(arr[mid]>=target):
#         return recursivelowerbound(arr,start,mid-1,target,mid)
#     else:
#         return recursivelowerbound(arr,mid+1,end,target,ans)
    
# print(recursivelowerbound(arr,0,len(arr)-1,9,ans))


# remove the ans varibale 

def recursivelowerbound(arr, start, end, target):
    if start > end:
        return start  # When target is not found, return the insertion point
    
    mid = (start + end) // 2
    
    if arr[mid] >= target:
        return recursivelowerbound(arr, start, mid - 1, target)
    else:
        return recursivelowerbound(arr, mid + 1, end, target)

arr = [1, 2, 3, 3, 7, 9, 9, 9, 11]
print(recursivelowerbound(arr, 0, len(arr) - 1, 12))  # Output should be 0

