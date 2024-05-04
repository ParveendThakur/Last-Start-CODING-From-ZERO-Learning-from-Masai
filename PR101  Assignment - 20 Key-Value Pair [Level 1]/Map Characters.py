# https://oj.masaischool.com/contest/11899?password=masai433

def solve(N):
    
    if 1 <= N <= 26:
        for i in range(N):
            alphabet = chr(ord('a') + i)  # Convert index to corresponding lowercase alphabet
            print(alphabet + '-' + str(i + 1))
    else:
        print("Invalid input. N should be between 1 and 26.")

  
