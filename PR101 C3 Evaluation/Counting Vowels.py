# https://oj.masaischool.com/contest/11917/problems

def solve(N,S):
    
    
    vowel_count = {'a' : 0, 'e' : 0, 'i' : 0, 'o' : 0, 'u' : 0}
    
    for char in S:
        
        if char in vowel_count:
            
            vowel_count[char] += 1
            
    print(vowel_count['a'], vowel_count['e'], vowel_count['i'], vowel_count['o'], vowel_count['u'], )        
  
