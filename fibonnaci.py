a=0
b=1
c=1
n=int (input("Enter number of terms : "))
print(a,end=",")
print(b,end=",")
for i in range(n-2):
    if i == (n-3):
        print(c,end=".")
        a=b
        b=c
        c=a+b
    else :
        print(c,end=",")
        a=b
        b=c
        c=a+b
        
