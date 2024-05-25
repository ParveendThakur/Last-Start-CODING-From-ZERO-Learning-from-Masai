# https://students.masaischool.com/assignments/39880?tab=assignmentDetails
# https://oj.masaischool.com/contest/12100/problems
# https://oj.masaischool.com/contest/12100/problem/01

#//Enter code here
def check_happiness(n, m, noodles, schedule):
    noodle_dict = {}
    for noodle in noodles:
        if noodle in noodle_dict:
            noodle_dict[noodle] += 1
        else:
            noodle_dict[noodle] = 1
    
    for day in schedule:
        if day in noodle_dict and noodle_dict[day] > 0:
            noodle_dict[day] -= 1
        else:
            return "ANGRY"
    
    return "HAPPY"

# Input
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    noodles = list(map(int, input().split()))
    schedule = list(map(int, input().split()))
    
    # Output
    print(check_happiness(n, m, noodles, schedule))


