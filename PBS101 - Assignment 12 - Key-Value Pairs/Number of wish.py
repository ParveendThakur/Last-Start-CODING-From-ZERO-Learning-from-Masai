# https://oj.masaischool.com/contest/11892?password=240203

def solve(N,string):
    
   # def solve(N, string):
    count = {'w': 0, 'i': 0, 's': 0, 'h': 0}  # Initialize count for each character in "wish"
    
    for char in string:
        if char in count:
            count[char] += 1
    
    # Find the minimum count of characters needed to form "wish"
    min_count = min(count.values())
    
    print(min_count)
