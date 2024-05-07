# https://oj.masaischool.com/contest/11917/problems

def solve(N,A):
    
    count = 0
    
    for i in range(1, N - 1):
        
        if A[i] > A[i - 1] and A[i] > A[i + 1]:
            count += 1
            
    print (count)        
    
