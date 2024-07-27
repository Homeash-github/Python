N = 1008
for i in range(N):
    if (i<10):
        if(i%2 == 0):
            print(i)
    else:
        T=i
        s=0
        while(T!=0):
            r=T%10
            s+=r
            T=T//10
        if (s%2 == 0):
            print(i)