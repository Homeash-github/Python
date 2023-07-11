a=eval(input("enter a string list : "))
l=len(a)
maxi=ind=0
for i in range(l):
    l2=len(a[i])
    
    if l2>maxi:
            maxi=l2
            ind=a[i]
print("largest string : ",ind)
    

