s=input("Enter a String:")
sub=input("Enter a substring:")
s=list(s)
sub=list(sub)
c=0
l1,l2=len(s),len(sub)
for i in range(l1):
	if(sub[0] == s[i]):
		if (sub[1:] == s[i+1:i+l2]):
			c+=1
			
print ("No of occurrence of given substring: ",c)
			
