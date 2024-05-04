def solve(N):
    
    #def map_symbols(N):
    symbol = N
    for i in range(8):
        if 1 <= N <= 126:  # Restricting the upper limit to avoid non-printable ASCII characters
            print(N)
            print(chr(symbol) + ' - ' + str(N))
            symbol += 2
            N += 2
        else:
            print("Invalid input. N should be between 1 and 126.")    
