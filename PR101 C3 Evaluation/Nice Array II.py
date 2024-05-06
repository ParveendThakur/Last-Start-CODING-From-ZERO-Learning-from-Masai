# https://students.masaischool.com/assignments/38812?tab=assignmentDetails
# https://oj.masaischool.com/contest/11917?password=evaluation3
# https://oj.masaischool.com/contest/11917/problems
# https://oj.masaischool.com/contest/11917/problem/01

def solve(N,array,K):
    
    odd = sum(1 for num in array if num % 2 != 0)
    
    if odd > K:
        print("Nice Array")
    else:
        print("Bad Array")
        
    
