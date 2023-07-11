for i in range (0,5):
    for j in range (0,5):
        if (i in range(0,5) and j%4==0)or(i==1 and j !=2)or(i==2 and j%2==0):
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
