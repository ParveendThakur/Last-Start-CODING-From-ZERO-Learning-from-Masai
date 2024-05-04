# https://oj.masaischool.com/contest/11892?password=240203

def solve(N,string):
    alp = "abcdefghijklmnopqrstuvwxyz"
    dic = {}
    for i in alp:
        dic[i] = 0
        
    #aeioua
    for i in string:
        dic[i] += 1
        
    print(*dic.values())  