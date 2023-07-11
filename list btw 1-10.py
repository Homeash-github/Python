l=eval(input("Enter a list from 1 to 12 : "))
le=len(l)
for i in range(le):
    if l[i]>=10:
        l[i]=10
print("New  list : ",l)
