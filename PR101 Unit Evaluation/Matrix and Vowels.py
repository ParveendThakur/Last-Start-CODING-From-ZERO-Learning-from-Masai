# https://oj.masaischool.com/contest/11949/problem/08

def solve(N,M,mat):
    
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    for col in range (M):
        vp = any(mat[row][col] in vowels 
        for row in range(N))
        if vp:
            print ("Yes")
        else:
            print ("No")
    

