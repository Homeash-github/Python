a=eval(input("Enter a list : "))
l=len(a)
for i in range(l):
    for j in range(0,(l-1-i)):
        if a[j]<a[j+1]:
            tmp=a[j]
            a[j]=a[j+1]
            a[j+1]=tmp
            
print(a)


    
        
