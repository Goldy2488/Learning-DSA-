# by normal recursin 

def twoParms(start,n):
    if(start>n):
        return
    print(n)
    twoParms(start,n-1)
print("By recursion answar :-")
twoParms(1,5)


# by backtracking

def oneParms(i,n):
    if(n<i):
        return 
    oneParms(i+1,n) 
    print(i)
print("By backtracking answar :-")
oneParms(1,5)