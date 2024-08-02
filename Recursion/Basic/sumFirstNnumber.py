# find sum of first N numbers
n = int(input("enter value of N :"))

# by parms
def sumOfN(n,sum):
    if(n==0):
        print(sum)
        return
    sum+=n
    sumOfN(n-1,sum)
sumOfN(n,0)

# by functional recursion
def funSumOfN(n):
    if(n==1):
        return 1
    return n+funSumOfN(n-1)
print("ans: ",funSumOfN(n))