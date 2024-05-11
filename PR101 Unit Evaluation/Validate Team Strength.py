# https://oj.masaischool.com/contest/11949/problem/03

def solve(n,k,arr):
    
    a = sum(arr[:n])
    b = sum (arr[n:])
    
    d = abs(a - b)
    
    if d <= k:
        print("Valid")
    else:
        print("Invalid")
    
