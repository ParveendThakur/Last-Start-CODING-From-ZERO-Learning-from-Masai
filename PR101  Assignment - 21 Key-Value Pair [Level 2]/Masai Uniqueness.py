def solve(s):
    

    # Create a set to store unique characters
    char_set = set()
    
    # Flag to track if all characters are unique
    all_unique = True
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is already in the set
        if char in char_set:
            all_unique = False
            break
        else:
            char_set.add(char)
    
    # Output
    if all_unique:
        print("UNIQUE")
    else:
        print("NO")

    
