t=eval(input("Enter a list of int type :  "))
l=len(t)
s=a=0
for i in range(l):
    b=len(t[i])
    for j in range(i):
        s+=t[0:l][i][j]
        a=s/b
    print("mean of index",i,"is",b)
