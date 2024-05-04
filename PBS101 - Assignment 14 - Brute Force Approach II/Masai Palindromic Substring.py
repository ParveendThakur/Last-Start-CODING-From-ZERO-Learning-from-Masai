# https://oj.masaischool.com/contest/11912?password=240203

def solve(s):
    
    
    # Function to find the length of the longest palindromic substring
#def longest_palindromic_substring(s):
    n = len(s)
    # Initialize a 2D table to store the results of subproblems
    dp = [[0] * n for _ in range(n)]

    # All substrings of length 1 are palindromes
    max_length = 1
    for i in range(n):
        dp[i][i] = 1

    # Check for substrings of length 2
    start = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = 1
            start = i
            max_length = 2

    # Check for substrings of length greater than 2
    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = 1
                if k > max_length:
                    start = i
                    max_length = k

    print(max_length) 
