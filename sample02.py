N = int(input())
L=[]
for i in range(N):
    a=input(':')
    if a=='print':
        print(L)
    elif 'insert' in a and a[-1] != ' ' and a[0] != ' ':
        L.insert(a[-3],a[-1])
    elif 'append' in a and a[-1] != ' ' and a[0] != ' ':
        L.append(a[-1])
    elif 'pop' in a and a[-1] != ' ' and a[0] != ' ':
        L.pop()
    elif 'sort' in a and a[-1] != ' ' and a[0] != ' ':
        L.sort()
    elif 'reverse' in a and a[-1] != ' ' and a[0] != ' ':
        L.reverse()
    elif 'remove' in a and a[-1] != ' ' and a[0] != ' ':
        L.remove(a[-1])
        
