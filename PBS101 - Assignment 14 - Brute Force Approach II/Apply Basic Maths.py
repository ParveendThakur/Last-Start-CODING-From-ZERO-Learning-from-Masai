# https://oj.masaischool.com/contest/11912?password=240203

def solve(N,A):
    
    #def find_index_to_remove(N, A):
    total_sum = sum(A)
    for i in range(N):
        if (total_sum - A[i]) % 7 == 0:
            print([i])
    print(-1)





  
