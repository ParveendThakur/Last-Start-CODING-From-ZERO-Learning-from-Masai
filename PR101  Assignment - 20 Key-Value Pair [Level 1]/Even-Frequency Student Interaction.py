def solve(n,arr):
    

# Create a dictionary to store the frequency of each student's interactions
    frequency = {}
    for student in arr:
        frequency[student] = frequency.get(student, 0) + 1

# Count the number of students with an even frequency of interactions
    count = 0
    for freq in frequency.values():
        if freq % 2 == 0:
            count += 1

# Print the count of students with even frequency of interactions
    print(count)
