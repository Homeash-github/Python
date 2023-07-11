L=[6,8,1,7,0,5,4]
l=len(L)
for i in range(l):
    m=i
    for j in range(i+1,l):
        if L[m]>L[j]:
            m=j
    L[i],L[m]=L[m],L[i]
print(L)