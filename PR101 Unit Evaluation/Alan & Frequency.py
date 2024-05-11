# https://oj.masaischool.com/contest/11949/problem/06

def solve(N,string):
    
    f = {}
    
    for char in string:
        if char in f:
            f[char] += 1
        else:
            f[char] =1
            
    for char in sorted(f):
        print(char + "-" + str(f[char]))
  
