# https://oj.masaischool.com/contest/12017/problem/4

#//Enter code here

def find_jersey_numbers(N, k, jerseys):
    left, right = 0, N - 1
    
    while left < right:
        total_jersey = jerseys[left] + jerseys[right]
        if total_jersey == k:
            return "Yes"
        elif total_jersey < k:
            left += 1
        else:
            right -= 1
    
    return "No"

# Reading input
T = int(input().strip())

for _ in range(T):
    N, k = map(int, input().split())
    jerseys = list(map(int, input().split()))
    result = find_jersey_numbers(N, k, jerseys)
    print(result)
