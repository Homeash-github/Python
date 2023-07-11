L=eval(input("Enter the list : "))
L.sort()
m=max(L)
sc=L[0]
for i in range (len(L)):
    if L[i]>sc and L[i]<m:
        sc=L[i]
print(sc)
