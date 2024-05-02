def solve(N,string):
    
    


# Count prime length substrings
    count = 0

# Function to check if a number is prime
    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        i = 3
        while i * i <= num:
            if num % i == 0:
                return False
            i += 2
        return True

# Iterate through all possible substrings
    for i in range(N):
        for j in range(i + 1, N + 1):
            length = j - i
            if length <= 1:
                continue
            prime = True
            for k in range(2, int(length ** 0.5) + 1):
                if length % k == 0:
                    prime = False
                    break
            if prime:
                count += 1

# Output
    print(count)
