# https://oj.masaischool.com/contest/11892?password=240203

def solve(N, arr):
    
    # Function to calculate the sum of unique elements in the array

    # Dictionary to store the count of each element
    count_dict = {}
    
    # Count occurrences of each element
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Calculate the sum of unique elements
    unique_sum = 0
    for num, count in count_dict.items():
        if count == 1:
            unique_sum += num
    
    print(unique_sum)
