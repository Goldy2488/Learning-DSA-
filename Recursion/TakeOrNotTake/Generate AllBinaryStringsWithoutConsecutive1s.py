#Q(from geeks for geeks) Generate all binary strings without consecutive 1’s
# Given an integer, K. Generate all binary strings of size k without consecutive 1’s.

# Examples: 

# Input : K = 3  :possible output: 000(v) 101(v) 010(v) 111(inValid) 110(invalid) 011(invalid) 100(valid) 001(valid)
# Output : 000 , 001 , 010 , 100 , 101 
# Input : K  = 4 
# Output :0000 0001 0010 0100 0101 1000 1001 1010

n = int(input("enter value n: "))
arr = []
def genBinaryStr(i,temp_str,n):
    if(i>=n):
        arr.append(temp_str)
        return 
    if(len(temp_str)==0 or temp_str[-1]=="0"):
        genBinaryStr(i+1,temp_str+"1",n)
        genBinaryStr(i+1,temp_str+"0",n)
    else:
        genBinaryStr(i+1,temp_str+"0",n)
genBinaryStr(0,"",n)
print(*arr)

# logic: if your last value is 0 the you take 1 or 0 both when last 
# value 1 need to take only 0 because if you are taking 1 then its will consecutive
# example : if you have 1 then you take 0 the output will be 10 other then the output 11 which is repeating 1.