L=[3,2,1,5,6,14,8]
l=len(L)
i=0
print(L)
while i<1:
    if L[i]%7==0:
        L[i],L[i+1]=L[i+1],L[i]
        i+=2
    else :
        i+=1
print(L)
