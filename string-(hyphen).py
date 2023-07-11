l=list(input("Enter a list : "))
L=len(l)
a=""
for i in range(L):
    a+=l[i]
print(a)
for j in range(L):
    if j != L-1:
        print(l[j],"--",end=" ")
    else :
        print(l[j])
