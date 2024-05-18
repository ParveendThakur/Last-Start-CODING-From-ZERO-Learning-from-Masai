# https://oj.masaischool.com/contest/12017/problem/3

#//Enter code here

def find_compounds_reactivity(N, x, compounds):
    left, right = 0, N - 1
    
    while left < right:
        total_reactivity = compounds[left] + compounds[right]
        if total_reactivity == x:
            return "Possible"
        elif total_reactivity < x:
            left += 1
        else:
            right -= 1
    
    return "Impossible"

# Reading input
T = int(input().strip())

for _ in range(T):
    N, x = map(int, input().split())
    compounds = list(map(int, input().split()))
    result = find_compounds_reactivity(N, x, compounds)
    print(result)
