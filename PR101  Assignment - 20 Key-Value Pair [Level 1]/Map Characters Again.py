def solve(N):
    
    for i in range(26):
        alphabet = chr(ord('a') + i)  # Convert index to corresponding lowercase alphabet
        print(alphabet + '-' + str(N))
        N += 1