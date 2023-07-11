
a=eval(input("Enter a list : "))
l=len(a)
maxi=0
indi=0
for i in range(l):
    b=a.count(a[i])
    
    if b>maxi:
        
            maxi=b
            indi=a[i]
print('mode is : ',indi) 
