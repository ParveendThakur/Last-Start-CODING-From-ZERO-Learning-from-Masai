def solve(N, K, s):
    

# Initialize the starting ASCII value for lowercase 'a'
    start_ascii = ord('a') - 1 + N

# Sum of mapped characters
    mapped_sum = 0

# Iterate over the characters in the string
    for char in s:
    # Map the character to its corresponding value
        mapped_value = ord(char) - ord('a') + start_ascii
        mapped_sum += mapped_value

# Output
    print(mapped_sum)

    
