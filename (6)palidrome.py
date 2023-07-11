a=input("Enter the word : ")
b=""
l=len(a)
for i in range(l):
    b=a[i]+b
if b==a:
    print("You have entered a pallindrome ! ! ! ")
else:
    print("You have not entered a pallindrome ! ! !")
