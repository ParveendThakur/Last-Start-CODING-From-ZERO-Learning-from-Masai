# https://oj.masaischool.com/contest/12027/problem/02

#//Enter code here

def max_sum_permutation(n,arr):
    arr.sort()
    max_sum = 0
    for i in range (n):
        max_sum += arr[i]*i
    return max_sum
    
n = int(input())
arr = list(map(int,input().split()))
print(max_sum_permutation(n,arr))