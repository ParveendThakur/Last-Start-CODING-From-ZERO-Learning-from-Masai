def custom_count(sequence, element):
    count = 0
    for item in sequence:
        if item == element:
            count += 1
    return count

# Test the function with list input
input_list = [1, 2, 2, 3, 4, 2]
search_element = 2
output_list = custom_count(input_list, search_element)
print(output_list)  # Output: 3

# Test the function with string input
input_string = 'hello world'
search_char = 'o'
output_string = custom_count(input_string, search_char)
print(output_string)  # Output: 2
