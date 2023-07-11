def bub(L):
    n=len(L)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if L[j]<L[min]:
                min=j
        if min != i:
            L[i],L[min]=L[min],L[i]
    
            
L=[64,23,65,132,98,10]
bub(L)
print(L)

                