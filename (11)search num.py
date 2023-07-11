n=int(input("Enter a number : "))
L=eval(input("enter a list : "))
l=len(L)
for i in range(l):
    if L[i]==n:
        print("Exist")
    else :
     print("Doesn't exist")
        
mini=min(L)
print(mini)
