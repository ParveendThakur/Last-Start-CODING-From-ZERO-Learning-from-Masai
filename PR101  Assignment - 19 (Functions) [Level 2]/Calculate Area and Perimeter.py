# https://students.masaischool.com/assignments/38650/problems/31772/134454

def rectangle_area(length, width):
"""
Calculates the area of a rectangle given its length and width.    
Args:
    - length (float): Length of the rectangle.
    - width (float): Width of the rectangle.
    
Returns:
    - float: Area of the rectangle.
"""
    return length * width

def rectangle_perimeter(length, width):
"""
Calculates the perimeter of a rectangle given its length and width.    
Args:
    - length (float): Length of the rectangle.
    - width (float): Width of the rectangle.
    
Returns:
    - float: Perimeter of the rectangle.
"""
    return 2 * (length + width)

# Example usage
length = 5
width = 3

area = rectangle_area(length, width)
perimeter = rectangle_perimeter(length, width)

print(f"Area of the rectangle: {area}")
print(f"Perimeter of the rectangle: {perimeter}")
