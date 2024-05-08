# https://students.masaischool.com/assignments/38864?tab=assignmentDetails
# https://oj.masaischool.com/contest/11933/problems
# https://oj.masaischool.com/contest/11933/problem/01

def solve(N,M,arr):
    
    

# Function to calculate the sum of even numbers in a column
    def sum_even_in_column(matrix, col):
        total = 0
        for row in matrix:
            if row[col] % 2 == 0:
                total += row[col]
        return total

# Iterate through each column and print the sum of even elements
    for j in range(M):
        print(sum_even_in_column(arr, j))

    
