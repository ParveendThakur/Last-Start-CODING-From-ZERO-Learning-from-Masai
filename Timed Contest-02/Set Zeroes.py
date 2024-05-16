# https://oj.masaischool.com/contest/12027/problem/05

#//Enter code here

def setZeroes(matrix):
    if not matrix:
        return
    
    rows , cols = len(matrix), len(matrix[0])
    zero_rows , zero_cols = set(),set()
    
    
    for i in range (rows):
        for j in range (cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)
                
    for row in zero_rows:
        for j in range (rows):
            matrix[row][j] = 0
            
            
    for col in zero_cols:
        for i in range (rows):
            matrix[i][col] = 0
            
            
            
n = int(input())
m,n=map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(m)]

setZeroes(matrix)

for row in matrix:
    print(*row)

