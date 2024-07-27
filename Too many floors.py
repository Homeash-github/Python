N=int(input())
for i in range (N):
    X,Y = map(int, input().split(" "))
    x=X//10
    y=Y//10
    if(X%10>0):
        x+=1
    if(Y%10>0):
        y+=1
    print(abs(y-x))