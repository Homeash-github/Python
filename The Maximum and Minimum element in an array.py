L=eval(input("Enter Array : "))
ma=L[-1]
mi=L[0]
for i in range(len(L)):
    if L[i]>ma:
        ma=L[i]
    if L[i]<mi:
        mi=L[i]
print("Maximum :",ma)
print("Minimum :",mi)