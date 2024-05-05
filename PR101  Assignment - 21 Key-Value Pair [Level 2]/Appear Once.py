def solve(N, arr):
    

# Create a dictionary to store the count of each element
    count_dict = {}
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

# Sum the elements that occur only once
    unique_sum = 0
    for num, count in count_dict.items():
        if count == 1:
            unique_sum += num

# Output
    print(unique_sum)

    
