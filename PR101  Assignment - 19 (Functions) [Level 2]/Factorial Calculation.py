# https://students.masaischool.com/assignments/38650/problems/31775/134456

def calculateFactorial(n):
    
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Example usage
result = calculateFactorial(5)
print("Result:", result)  # Output: 120
