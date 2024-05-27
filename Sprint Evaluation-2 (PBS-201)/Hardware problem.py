# https://students.masaischool.com/assignments/39905?tab=assignmentDetails
# https://oj.masaischool.com/contest/12101/problems
# https://oj.masaischool.com/contest/12101/problem/101-100

#//Enter code here
def fdc(N,D,times):
    for i in range (N-1):
        if 2* times[i] - times [i + 1] <= D:
            return times[i + 1]
            
    return -1
    

t = int (input().strip())

for _ in range (t):
    
    N,D = map(int , input().strip().split())
    times = list(map(int,input().strip().split()))
    
    result = fdc(N,D,times)
        
    print(result)