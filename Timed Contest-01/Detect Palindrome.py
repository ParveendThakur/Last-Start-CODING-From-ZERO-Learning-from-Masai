# https://students.masaischool.com/assignments/39086?tab=assignmentDetails
# https://oj.masaischool.com/contest/11994/problems
# https://oj.masaischool.com/contest/11994/problem/01

# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)         # Writing output to STDOUT
num = int(input())
ns = str(num)
if ns == ns[::-1]:
    print("Yes")
else:
    print("No")
