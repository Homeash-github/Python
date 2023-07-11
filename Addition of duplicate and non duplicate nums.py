sum1=sum2=0
n1=int(input("Enter number 1 :"))
n2=int(input("Enter number 2 :"))
n3=int(input("Enter number 3 :"))
sum1=n1+n2+n3
if n1 != n2 and n1 != n3 and n2 != n3:
   sum2=n3+n1+n2
elif n1 == n2 and n1 != n3 :
   sum2=n3+n1
elif n1 != n2 and n1 == n3 :
   sum2=n2+n1   
elif n2 != n1 and n2 == n3 :
   sum2=n1+n2
else:
   sum2=n1
print("numbers are ",n1,n2,n3)
print("Sum of three given number is :",sum1);
print("Sum of non duplicate numbers are :",sum2);
