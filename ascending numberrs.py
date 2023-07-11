a=int(input('enter first number : '))
b=int(input('enter second number : '))
c=int(input('enter third number : '))
if  a>b and a>c:
    if b>c :
        big=a
        mid=b
        sml=c
    else :
        big=a
        mid=c
        sml=b
elif b>a and b>c:
    if a>c:
        big=b
        mid=a
        sml=c
    else:
        big=b
        mid=c
        sml=a
elif c>b and c>a:
    if b>a:
        big=c
        mid=b
        sml=a
    else:
        big=c
        mid=a
        sml=b
print("The Numbers in Ascending order : ",sml,mid,big)
