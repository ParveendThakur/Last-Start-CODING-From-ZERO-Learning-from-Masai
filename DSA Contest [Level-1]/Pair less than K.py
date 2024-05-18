# https://oj.masaischool.com/contest/12017/problem/5

def find_max_S_less_than_K(N, A, K):
    A.sort()
    max_S = -1
    left, right = 0, N - 1
    
    while left < right:
        total_S = A[left] + A[right]
        if total_S < K:
            max_S = max(max_S, total_S)
            left += 1
        else:
            right -= 1
    
    return max_S

# Reading input
T = int(input().strip())

for _ in range(T):
    N = int(input().strip())
    A = list(map(int, input().split()))
    K = int(input().strip())
    result = find_max_S_less_than_K(N, A, K)
    print(result)
