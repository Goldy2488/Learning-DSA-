# Fibonacci
# 0 1 1 2 3 5 8 13 21 34....

# find the nth fibonacci number
n= int(input("enter value of N : "))

def fib(n):
    if  n<=1:
        return n
    return fib(n-1)+fib(n-2)
print(fib(n))

# stack
# fib(3)-->2
#   fib(2)-->1  + fib(1)-->1
    # fib(1) -->1


# fib(2) -->1
    # fib(1)-->1 + fib(0)-->0


# Time complexity : 2^n==>2^2