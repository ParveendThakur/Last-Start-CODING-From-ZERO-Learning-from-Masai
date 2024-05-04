# https://students.masaischool.com/assignments/38738/problems/33271/134566

def custom_slice(lst, start, end):
    # Handle negative indices
    if start < 0:
        start += len(lst)
    if end < 0:
        end += len(lst)
    
    # Slice the list using the start and end indices
    return lst[start:end]

# Test the function
input_list = [1, 2, 3, 4, 5]
start_index = 1
end_index = 4
output = custom_slice(input_list, start_index, end_index)
print(output)  # Output: [2, 3, 4]
