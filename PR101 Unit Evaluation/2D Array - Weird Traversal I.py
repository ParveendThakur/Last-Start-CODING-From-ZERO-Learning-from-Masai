# https://oj.masaischool.com/contest/11949/problem/09

def solve(N,arr):
        
    c1 = sum(arr[i][0] for i in range (N // 2))
    
    c2 = sum(arr[N // 2])
    
    c3 = sum (arr[i][N-1] for i in range (N // 2 , N))
    
    out = 3*c1 + c2 + 2*c3
    
    print(out)
    
    
