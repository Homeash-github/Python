for i in range (0,6):
    for j in range (0,8):
        if (i in range(0,5) and j%5==0)or(i==2 and j in range (0,8)):
            print("*",end="")
        else :
            print(" ",end=" ")
    print()
