# https://students.masaischool.com/assignments/39250?tab=assignmentDetails
# https://oj.masaischool.com/contest/12017/problems
# https://oj.masaischool.com/contest/12017/problem/1

#//Enter code here

def such_pair_returns(N, K, integers):
    seen = set()
    for num in integers:
        complement = K - num
        if complement in seen:
            return 1
        seen.add(num)
    return -1

# Input processing
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    integers = list(map(int, input().split()))
    
    result = such_pair_returns(N, K, integers)
    print(result)
