A=eval(input("Enter a list : "))
l=len(A)
temp=0
B=[]
B.append(A[-1])
for i in range(0,l-1):
    B.append(A[i])   
print(B)
