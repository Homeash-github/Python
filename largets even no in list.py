a=eval(input("Enter a list : "))
l=len(a)
b=[]
print("Enter the original list : ",a )
for i in range(l):
    maxi=0
    indi=i
    if a[i]%2==0:
        c=b.append(a[i])  
        c=len(b)
        if c!=0:
            for j in range(c):
                if b[j]>maxi:
                    maxi=b[j]
                    indi=j
            print("The largest even number : ",maxi)
            break
else:
    print("there is no even number in list ")



