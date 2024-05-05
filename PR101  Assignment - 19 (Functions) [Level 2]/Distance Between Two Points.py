# https://students.masaischool.com/assignments/38650?tab=assignmentDetails
# https://drive.google.com/drive/folders/17ksLOE4BMf2-oH7JR4FY8n8V63kvCxaZ?usp=sharing
# https://students.masaischool.com/assignments/38650/problems/31770/134452

import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Sample Input
point1 = (2, 3)
point2 = (5, 7)

# Unpack the coordinates
x1, y1 = point1
x2, y2 = point2

# Calculate distance
result = distance(x1, y1, x2, y2)
print(result)  # Output: 5.0
