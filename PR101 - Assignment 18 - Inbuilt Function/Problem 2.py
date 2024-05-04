# https://students.masaischool.com/assignments/38738/problems/33271/134566

def custom_rindex(lst, item):
    for i in range(len(lst) - 1, -1, -1):  # Iterate from the end of the list backwards
        if lst[i] == item:
            return i
    return -1  # Return -1 if the item is not found

# Test the function
input_list = [1, 2, 3, 2, 4]
search_item = 2
output = custom_rindex(input_list, search_item)
print(output)  # Output: 3
