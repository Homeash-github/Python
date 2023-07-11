def fact(n=int(input("Enter a number : "))):
    f=1
    for i in range(1,n+1,1):
        f=f*i
    print("FACTORIAL = ",f)
fact()
    
