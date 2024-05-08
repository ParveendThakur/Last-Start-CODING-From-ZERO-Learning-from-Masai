# https://oj.masaischool.com/contest/11933/problems

def solve(N,arr):
    

    
    z_traverse = []
    for i in range(N):
        if i % 2 == 0:  # even rows
            for j in range(N):
                z_traverse.append(str(N[j][i]))
        else:  # odd rows
            for j in range(N - 1, -1, -1):
                z_traverse.append(str(N[j][i]))

    result = ''.join(z_traverse)
    print(result)

    
