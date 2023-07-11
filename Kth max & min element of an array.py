k=int(input("Enter Value for 'K' : "))
L=eval(input("Enter a Array : "))
l=len(L)
L.sort()
vma=L[-k]
vmi=L[k-1]
print(f"The {k}th largest element is {vma}")
print(f"The {k}th smallest element is {vmi}")