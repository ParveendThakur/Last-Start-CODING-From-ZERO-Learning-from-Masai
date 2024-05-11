# https://oj.masaischool.com/contest/11949/problem/04

def solve(N,string):
    
    v = sum(1 for char in string if char.lower() in 'aeiou')
    c = N-v
    
    p = 7*v+2*c
    
    print(p)
  
