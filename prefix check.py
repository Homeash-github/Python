name=input("Enter a  word : ")
s=input("Enter a substring : ")
m=len(s)
l=len(name)
if (name[0:m]==s):
    print(s,"is a prefix of",name)
else :
    print(s,"is not a prefix of",name)

