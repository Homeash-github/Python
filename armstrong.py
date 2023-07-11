a=int(input("Enter a number : "))
A=a
s=0
while A!= 0:
    x=A%10
    A=int(A/10)
    s=s+(x**3)
if s==a:
    print("It is armstrong no: ")
else :
    print("It is not armstrong no:")
