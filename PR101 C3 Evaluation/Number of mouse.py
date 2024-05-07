# https://oj.masaischool.com/contest/11917/problems

def solve(N,S):
    
    char_count = {}
    for char in S:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    
    max_count = float('inf')
    mouse_chars = {'m' : 1, 'o' : 1, 'u' : 1, 's' : 1, 'e' : 1}
    for char, count in mouse_chars.items():
        if char in char_count:
            max_count = min(max_count, char_count[char] // count)
        else:
            max_count = 0
            break
        
    print(max_count)    
        
        
  
