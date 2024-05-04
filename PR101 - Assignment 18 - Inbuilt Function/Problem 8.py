def custom_reverse(sequence):
    if isinstance(sequence, list):
        return list(reversed(sequence))
    elif isinstance(sequence, str):
        return sequence[::-1]
    else:
        raise TypeError("Sequence must be a list or a string")

# Test the function with list input
input_list = [1, 2, 3, 4, 5]
output_list = custom_reverse(input_list)
print(output_list)  # Output: [5, 4, 3, 2, 1]

# Test the function with string input
input_string = 'hello'
output_string = custom_reverse(input_string)
print(output_string)  # Output: 'olleh'
