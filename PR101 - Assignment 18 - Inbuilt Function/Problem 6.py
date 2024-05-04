def custom_index(lst, value):
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    raise ValueError("Value not found in list")

# Test the function
input_list = [1, 2, 3, 4, 5]
search_value = 3
try:
    output = custom_index(input_list, search_value)
    print(output)  # Output: 2
except ValueError as e:
    print(e)
