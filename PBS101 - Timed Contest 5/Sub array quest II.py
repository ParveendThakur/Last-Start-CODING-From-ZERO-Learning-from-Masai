def solve(N,A):
    
    
    # Function to count subarrays starting and ending with even numbers
    def count_subarrays(arr):
        N = len(arr)
        count = 0
        even_count = 0
    
        for i in range(N):
            if A[i] % 2 == 0:
                even_count += 1
                count += even_count
    
        return count

    
        # Counting subarrays and printing the result
        subarray_count = 0
        for i in range(N):
            if A[i] % 2 == 0:
                for j in range(i, n):
                    if arr[j] % 2 == 0:
                        subarray_count += 1

        print(subarray_count)

