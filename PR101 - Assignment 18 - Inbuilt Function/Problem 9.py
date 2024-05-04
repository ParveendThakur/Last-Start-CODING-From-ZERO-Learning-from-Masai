# https://students.masaischool.com/assignments/38738/problems/33271/134566
# Questions Link : Click here
# https://masai-school.notion.site/Inbuilt-Functions-eb495df093a94ff7847d0632bf5cfc31

def custom_find(string, substring):
    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            return i
    return -1

# Test the function
input_string = 'Look for the substring in this string.'
search_substring = 'substring'
output = custom_find(input_string, search_substring)
print(output)  # Output: 12
