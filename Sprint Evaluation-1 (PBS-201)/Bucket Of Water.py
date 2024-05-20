# https://students.masaischool.com/assignments/39404?tab=assignmentDetails
# https://oj.masaischool.com/contest/12023/problems
# https://oj.masaischool.com/contest/12023/problem/101-100

#//Enter code here

def cpw(N, a, b):
    tw = sum(a)
    tc = sum(b)
    mc = max(b)
    
    if tw <= tc:
        return "Yes"
    if tw > mc:
        return "No"
        
    count = 0
    
    for i in range (N):
        if b[i] - a[i] >= tw - mc:
            count += 1
            if count == 2:
                return "Yes"
    return "No"            
    

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        a = list(map(int , input().split()))
        b = list(map(int , input().split()))
        
        print (cpw(N, a, b))
    
    
    
    