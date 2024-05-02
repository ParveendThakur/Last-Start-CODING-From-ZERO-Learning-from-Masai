def solve(a,b):
    

# Check if a number is prime
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

# Check if both a and b are prime
    if is_prime(a) and is_prime(b):
        print(True)
    else:
        print(False)

  
