a=eval(input("Enter a list : "))
a.sort()
l=len(a)
med=b=c=0
for i in range(l):  
    if l%2==0:
        b=int((l-1)/2)
        c=int((l+1)/2)
        med=((a[b]+a[c])/2)
    else :
        b=int(((l-1)/2)+0.5)
        med=(a[b])
print("The median of the list : ",med)
    
