name=input("Enter your name : ")
c=input("Enter any character : ")
l=len(name)
count=0
for i in range (l):
    if name[i]==c:
        count+=1
print("the frequency of",c,"in",name,"is :",count)
