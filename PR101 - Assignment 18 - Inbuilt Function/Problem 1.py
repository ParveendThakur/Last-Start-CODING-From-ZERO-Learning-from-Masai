# https://students.masaischool.com/assignments/38738/problems/33271/134566
# Questions Link : Click here
# https://masai-school.notion.site/Inbuilt-Functions-eb495df093a94ff7847d0632bf5cfc31

def custom_join(strings, separator):
    # Check if the input list is empty
    if not strings:
        return ''
    
    # Initialize an empty string to store the result
    result = strings[0]
    
    # Concatenate each element of the list with the separator
    for string in strings[1:]:
        result += separator + string
    
    return result

# Test the function
input_list = ['Hello', 'World']
separator = ' '
output = custom_join(input_list, separator)
print(output)  # Output: 'Hello World'
