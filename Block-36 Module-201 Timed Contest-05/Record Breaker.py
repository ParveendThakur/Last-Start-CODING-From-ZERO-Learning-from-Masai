# https://students.masaischool.com/assignments/40195?tab=assignmentDetails
# https://oj.masaischool.com/contest/12166/problems
# https://oj.masaischool.com/contest/12166/problem/01

#//Enter code here

def record_breaker(scores):
    if not scores:
        return 0, 0
    
    max_score = scores[0]
    min_score = scores[0]
    max_breaks = 0
    min_breaks = 0
    
    for i in range(1, len(scores)):
        if scores[i] > max_score:
            max_score = scores[i]
            max_breaks += 1
        if scores[i] < min_score:
            min_score = scores[i]
            min_breaks += 1
    
    return max_breaks, min_breaks

# Input
T = int(input().strip())

for _ in range(T):
    n = int(input().strip())
    scores = list(map(int, input().strip().split()))
    
    max_breaks, min_breaks = record_breaker(scores)
    print(max_breaks, min_breaks)
