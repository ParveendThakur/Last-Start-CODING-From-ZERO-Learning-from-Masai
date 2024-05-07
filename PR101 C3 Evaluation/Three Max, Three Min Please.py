# https://oj.masaischool.com/contest/11917/problems

def solve(N,A):
    
    A.sort()
    
    mini = sorted(set(A[:3]))
    maxi = sorted(set(A[-3:]))
    
    min_count = 0
    max_count = 0
    
    for num in A:
        if num in mini:
            min_count += 1
        if num in maxi:
            max_count += 1
    
    if min_count < N:
        print("Not Possible")
        
    else:
        for value in mini:
            print(value , end=" ")
        print ()    
    
    if maxi < N:
        print("Not Possible")
    else:
        for value in maxi:
            print(value , end=" ")
        print () 
    
