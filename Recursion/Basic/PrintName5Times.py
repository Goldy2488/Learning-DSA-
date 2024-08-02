# Print name 5 times
def intro(name,n):
    if(n<1):
        return
    print(name,n)
    intro(name,n-1)

intro("Goldy",5)