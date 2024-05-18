# https://oj.masaischool.com/contest/12017/problem/2

#//Enter code here

def count_pairs_with_sum(arr, target):
    pair_count = 0
    num_counts = {}
    
    for num in arr:
        complement = target - num
        if complement in num_counts:
            pair_count += num_counts[complement]
        num_counts[num] = num_counts.get(num, 0) + 1
    
    return pair_count

# Reading input
N, K = map(int, input().split())
arr = list(map(int, input().split()))

# Calculate and print the count of pairs whose sum is K
print(count_pairs_with_sum(arr, K))
