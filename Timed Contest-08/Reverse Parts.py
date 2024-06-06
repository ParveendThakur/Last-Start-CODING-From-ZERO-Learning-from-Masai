# https://students.masaischool.com/assignments/40541?tab=assignmentDetails
# https://oj.masaischool.com/contest/12257/problems
# https://oj.masaischool.com/contest/12257/problem/01

#//Enter code here

def rp(N, s, L, R):
    
    substring = s[L:R+1]
    
   
    rs = substring[::-1]
    
   
    updated_string = s[:L] + rs + s[R+1:]
    
    return updated_string

# Input
N = int(input())
s = input().strip()
L, R = map(int, input().split())

# Output
print(rp(N, s, L, R))
