
T=int(input())
for i in range(T):
    N,X=map(int,input().split(" "))
    c=0
    L=list(map(int,input().split(" ")))
    for i in L:
        if (i>=X):
            c+=1
    print(c)    
        