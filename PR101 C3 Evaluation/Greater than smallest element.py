# https://oj.masaischool.com/contest/11917/problems

def solve(N,A):
    
    m = min(A)
    
    for i in range(N):
        if A [i] > m:
            A[i] = -1
    
    print(*A)        
    
