# https://oj.masaischool.com/contest/11949/problem/07

def solve(N,A):
    
    freq_map = {}
    
    for num in A:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1
            
    max_freq_element = None
    max_freq = -1
    
    for num, freq in freq_map.item():
        if freq > max.freq or (freq == max.freq 
        and A.index(num) < arr.index(max.freq_element)):
            max_freq_element = num
            max_freq = freq
            
    print(max_freq_element)        
         
    
