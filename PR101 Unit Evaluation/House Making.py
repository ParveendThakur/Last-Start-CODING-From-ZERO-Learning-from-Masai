# https://students.masaischool.com/assignments/38959?tab=assignmentDetails
# https://oj.masaischool.com/contest/11949/problems
# https://oj.masaischool.com/contest/11949/problem/01

def solve(N,K):
    
    b = N*K
    if b >= 1000 and b % 5 ==0:
        print("yes")
    else:
        print("no")
  
