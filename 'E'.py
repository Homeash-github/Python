for i in range (0,5):
    for j in range (0,5):
        if (i%2==0  and j in range(0,4) )or(i%2!=0 and j==0):
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
