# https://oj.masaischool.com/contest/11949/problem/05

def solve(N,string):
    
    count = sum(1 for char in string if char.isupper())
    
    r = 13*count
    
    print(r)
  
