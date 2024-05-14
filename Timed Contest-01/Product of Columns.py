# https://oj.masaischool.com/contest/11994/problem/02

# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)         # Writing output to STDOUT

N = 3
M = 2
arr = [[1,2], [3,4], [5,6]]

for j in range (M):
    product = 1
    for i in range (N):
        product *= arr[i][j]
    print(product)    