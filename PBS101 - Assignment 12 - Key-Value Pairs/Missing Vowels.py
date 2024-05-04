# https://oj.masaischool.com/contest/11892?password=240203

def solve(N,string):
    
    
    vowels = {'a', 'e', 'i', 'o', 'u'}
    present_vowels = set(string)
    
    missing_vowels = vowels - present_vowels
    
    if len(missing_vowels) == 0:
        print("-1")
    else:
        print(''.join(sorted(missing_vowels)))

