a=input("Enter the word : ")
b=""
l=len(a)
for i in range(l):
    b=a[i]+b
if b==a:
    print("You have entered a pallindrome ! ! ! ")
else:
    print("You have not entered a pallindrome ")
    c=a
    for j in range(-1,-l-1,-1):
        c+=a[j]
    print("The new pallindromed word is ",c)
