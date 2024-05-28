# https://oj.masaischool.com/contest/12166/problem/02

# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)         # Writing output to STDOUT

def merge_sorted_arrays(arr1, arr2):
    merged_array = []
    i = 0
    j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1
    
    return merged_array

# Input
N = int(input().strip())
arr1 = list(map(int, input().strip().split()))
arr2 = list(map(int, input().strip().split()))

# Merge the sorted arrays
result = merge_sorted_arrays(arr1, arr2)

# Output
print(*result)
