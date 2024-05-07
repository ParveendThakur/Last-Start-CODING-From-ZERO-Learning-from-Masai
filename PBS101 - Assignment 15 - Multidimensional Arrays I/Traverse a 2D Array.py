# https://students.masaischool.com/assignments/38857?tab=assignmentDetails
# https://oj.masaischool.com/contest/11930/problems
# https://oj.masaischool.com/contest/11930/problem/01

def solve(N,M,arr):
    
    # Input
#N, M = map(int, input().split())
#matrix = [list(map(int, input().split())) for _ in range(N)]

# Traversing and printing in the zigzag pattern
    for i in range(N):
        if i % 2 == 0:
            for j in range(M):
                print(arr[i][j], end=' ')
        else:
            for j in range(M - 1, -1, -1):
                print(arr[i][j], end=' ')

    
