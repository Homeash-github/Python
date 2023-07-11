a=eval(input("Enter a list : "))
l=len(a)
b=c=0
for i in range(l):
    if a[i]%2==0:
        b+=a[i]
        
    else :
        c+=a[i]
        
print("The sum of even index : ",b)
print("The sum of odd index : ",c)
