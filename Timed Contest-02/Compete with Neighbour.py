# https://students.masaischool.com/assignments/39270?tab=assignmentDetails
# https://oj.masaischool.com/contest/12027/problems
# https://oj.masaischool.com/contest/12027/problem/01

#//Enter code here

def count_larger_then_neighbord(arr):
    count = 0
    for i in range (1 , len (arr) -1):
        if arr [i]>arr[i-1] and arr [i]>arr[i+1]:
            count +=1
    return count
    
n = int(input())
arr = list(map(int,input().split()))
print(count_larger_then_neighbord(arr))