def solve(N):
    
    total = 80
    if N<=50:
        print(N*3+80)
    elif N<=150:
        print(total + (50*3) + ((N-50)*5))
    else :
        print(total + (50*3)+ (100*5)+ (N-150)*10)
    
