# https://oj.masaischool.com/contest/11949/problem/02

def solve(N, arr):
    
    mid = N // 2
    
    sum_f_h = sum(arr[:mid])
    sum_s_h = sum(arr[mid:])
    
    r = 7*sum_f_h + 2 * sum_s_h
    
    print(r)
    
    
