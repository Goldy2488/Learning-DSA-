# by normal recursion
def linear(start,n):
    if start>n:
        return
    print(start)
    linear(start+1,n)
print("by normal recursion :-")
n=int(input("enter your end number: "))
linear(1,n)


# by backtracking
def linear(n):
    if(n==0):  
        return 
    linear(n-1)
    print(n)
print('by backtracking :- ')
linear(5)