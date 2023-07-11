L=eval(input("Enter a list : "))
l=len(L)
l1=[]
l2=[]
for i in L:
    if i not in l2:
        c=L.count(i)
        l1.append(c)
        l2.append(i)
print("Element \t\t\t Frequency")
for i in range(len(l2)):
    print(l2[i],' \t\t\t ',l1[i])
