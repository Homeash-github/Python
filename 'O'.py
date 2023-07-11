for i in range (0,7):
    for j in range(0,7):
        if(i==0 and j in range(2,5))or(i+j==2)or(j-i==4)or(i==3 and j%6==0)or(i-j==4)or(i+j ==10)or(i==6 and j in range(2,5)):
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
