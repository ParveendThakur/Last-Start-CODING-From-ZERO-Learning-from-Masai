# https://oj.masaischool.com/contest/11912?password=240203

def solve(N,A):
    
    total_sum = 0
    for i in range(N):
        for j in range(i + 1, N):
            if (j - i):
                total_sum += abs(A[j] - A[i])
    print(total_sum)

  
