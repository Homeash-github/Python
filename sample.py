x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))
n = int(input('n: '))
L=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            l=[]
            if i+j+k != n:
                l.append(i)
                l.append(j)
                l.append(k)
            L.append(l)
#print(L)
A=[]
for i in L:
    if len(i)!=0:
        A.append(i)
print(A)