string = input("Enter a Any value : ")
n = len(string)

def swap(s,e,charList):
    temp = charList[s]
    charList[s] = charList[e]
    charList[e] = temp

def reverse(start,charList):
    if(start>=n//2):
        return "".join(charList)
    swap(start,n-start-1,charList)
    return reverse(start+1,charList)


def isPalindrome(string):
    reverseVal = reverse(0,list(string))
    if(string == reverseVal):
        return True
    else:return False
print(isPalindrome(string))
