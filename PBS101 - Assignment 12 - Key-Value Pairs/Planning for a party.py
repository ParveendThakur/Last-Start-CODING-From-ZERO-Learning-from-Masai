# https://oj.masaischool.com/contest/11892?password=240203

def solve(N,A,M,B):
    
    N = set(A)
    M = set(B)
    
    if N == M:
        print("Yes")
    else:
        print("No")