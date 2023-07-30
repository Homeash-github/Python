N = int(input())
L=[]
for i in range(N):
    a=input()
    w=[]
    w=a.split()
    if ("insert" in a):
        L.insert(int(w[-2]),int(w[-1]))
    elif ("append" in a):
        L.append(int(w[-1]))
    elif ("remove" in a):
        L.remove(int(w[-1]))
    elif ("print" in a):
        print(L)
    elif ("sort" in a):
        L.sort()
    elif ("reverse" in a):
        L.reverse()
    elif ("pop" in a):
        L.pop()
