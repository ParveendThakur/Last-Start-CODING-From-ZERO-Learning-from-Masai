# https://oj.masaischool.com/contest/11949/problem/10

def solve(n,m,p,matrix):
    
    count=0
    
    # hori
    for i in range (n):
        for j in range (m - 2):
            product = matrix[i][j]*matrix[i][j+1] * matrix[i][j+2]
            if product == p:
                count += 1
    
    # vert
    for i in range (n - 2):
        for j in range(m):
            product = matrix[i][j]*matrix[i+1][j] * matrix[i+2][j]
            if product == p:
                count += 1 
    
    #digo t-l to b-r
    for i in range (n - 2):
        for j in range(m-2):
            product = matrix[i][j] * matrix[i+1][j+1] * matrix[i+2][j+2]
            if product == p:
                count += 1 
                
    #digo b-l to t-r
    for i in range (2, n):
        for j in range(m-2):
            product = matrix[i][j] * matrix[i-1][j+1] * matrix[i-2][j+2]
            if product == p:
                count += 1             
    
    
    
    print(count)
    
    
    
