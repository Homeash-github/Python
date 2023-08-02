p=[]
n=int(input("enter n: "))
for i in range(1,n):
    c=0
    for j in range(1,i+1):
        if (i%j == 0):
            c+=1
    if (c==2 ):
        print(i)
        p.append(i)
p=p[::-1]
# print(p)
l=[]
for k in p:
    if (n%k == 0):
        l.append(k)
print(l[0])        

