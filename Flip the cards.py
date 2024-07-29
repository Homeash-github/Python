N = int(input())
for i in range(N):
    X,Y = map(int, input().split(" "))
    mid=X//2
    if(Y<=mid):
        print(Y)
    else:
        print(abs(X-Y))