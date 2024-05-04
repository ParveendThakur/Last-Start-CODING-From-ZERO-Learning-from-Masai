def custom_substring(string, start, end):
    # Slice the string using the start and end indices
    return string[start:end]

# Test the function
input_string = 'Hello, World!'
start_index = 7
end_index = 12
output = custom_substring(input_string, start_index, end_index)
print(output)  # Output: 'World'
