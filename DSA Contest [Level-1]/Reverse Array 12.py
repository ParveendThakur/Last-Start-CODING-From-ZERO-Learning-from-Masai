# https://oj.masaischool.com/contest/12017/problem/6

#//Enter code here

# Reading input
n = int(input().strip())
arr = list(map(int, input().split()))

# Reversing the array using slicing and printing the result
reversed_arr = arr[::-1]
print(*reversed_arr)
