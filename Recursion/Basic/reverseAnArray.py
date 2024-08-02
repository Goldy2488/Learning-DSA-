# Reverse AN array
arr = [2,3,4,5,6,6,7]
# by loop 
print('by loop :')
# return swap value
def swap(start,end):
    temp= arr[end]
    arr[end] = arr[start]
    arr[start] = temp

def reverseByLoop(s,e):
    while s<e:
        swap(s,e)
        s+=1
        e-=1
reverseByLoop(0,len(arr)-1)
print(arr)

# by recursion 
def reverseByRecursion(s,e):
    if (s>=e):
        return
    swap(s,e)
    reverseByRecursion(s+1,e-1)

reverseByRecursion(0,len(arr)-1)
print(arr)

# By single variable 
n=len(arr)
def reverseByUseSingleVar(s):
    if(s>=n/2):
        return
    swap(s,n-s-1)
    reverseByUseSingleVar(s+1)
reverseByUseSingleVar(0)
print(arr)
