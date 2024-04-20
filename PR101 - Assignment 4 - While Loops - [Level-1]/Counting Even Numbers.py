def count_even_numbers(N):
    count = 0
    i = 1
    while i<=N:
        if (i%2==0):
            count+=1
            #print (i)
        i+=1
    print(count)    
    
