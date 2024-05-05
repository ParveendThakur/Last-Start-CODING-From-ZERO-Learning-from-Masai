# https://oj.masaischool.com/contest/11900?password=masai2804

def solve(N, A):
    

# Create a dictionary to store the count of each integer
    count_dict = {}
    for num in A:
        if num in count_dict:
            count_dict[num] += 1
    else:
        count_dict[num] = 1

# Find the integer with the maximum count
    max_count = 0
    max_num = None
    for num, count in count_dict.items():
        if count > max_count:
            max_count = count
            max_num = num

    # Output
    print(max_num)
