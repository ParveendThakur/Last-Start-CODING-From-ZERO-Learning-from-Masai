def solve(N,string):
    
    

# Initialize counts for vowels and consonants
    vowels_count = 0
    consonants_count = 0

# Iterate through the characters of the string
    for char in string:
        if char in 'aeiou':
            vowels_count += 1
        else:
            consonants_count += 1

# Check the counts and print the result
    if vowels_count == consonants_count:
        print("Tie")
    elif vowels_count > consonants_count:
        print("Vowel")
    else:
        print("Consonant")

  
