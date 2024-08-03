# Subsequence => it can contiqous or non contiqous sequences *which follow the order* 
# arr = [3,1,2]
# ans =>    
# 3
# 1
# 2
# 3 1
# 1 2
# 3 2 = non contiqous
# 3 1 2
# []
# total 8 subsequence
# https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/


# Function to print all subsets of the array using recursion
def sub(inx, temp_arr):
    if inx >= n:  # Base case: if index is out of bounds, print the current subset
        print(temp_arr)
        return
    temp_arr.append(arr[inx])  # Include the current element in the subset
    sub(inx + 1, temp_arr)  # Recurse with the next index
    temp_arr.remove(arr[inx])  # Exclude the current element and backtrack
    sub(inx + 1, temp_arr)  # Recurse with the next index

arr = [3, 1, 2]  # Input array
n = len(arr)  # Length of the array
sub(0, [])  # Start the recursion with the initial index 0 and empty subset

# power set
arr = []
print(arr[-1])