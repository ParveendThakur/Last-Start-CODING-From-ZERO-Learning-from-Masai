# https://oj.masaischool.com/contest/11917/problems

def solve(S):
    
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    consonant_count = 0
    
    for char in S:
        
        if char.isalpha() and char.lower() not in vowels:
            consonant_count += 1
            
            
    print(consonant_count)        
            
  
