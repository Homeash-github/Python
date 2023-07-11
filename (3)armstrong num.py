n=int(input("Enter a number : "))
b=n
s=0
a=0

while b != 0 :
    a=int(b%10)
    b=int(b/10)
    s+=a**3
if s==n:
    print(n,"is an ARMSTRONG NUMBER ")
else :
    print(n,"is not an ARMSTRONG NUMBER ")
