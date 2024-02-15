a=input("Enter no:")
L=[]
for s in a:
    L.append(int(s))
print(L)
l=len(L)
for i in range(l):
    for j in range(l):
        if (i==j):   
            print(L[i],end=" ")
        if (i+j == l-1 and (i and j)!=int(l/2)):
            print(L[-i-1],end=" ")
        else:
            print(" ",end=" ")
    print()