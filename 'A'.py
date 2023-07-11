for i in range(0,4):
    for j in range(0,7):
        if  (i==0  and  j==3) or  (i==1 and  j ==2 ) or  (i==1  and  j==4) or (i==2 and j in range(1,5)) or (i==3 and j==0) or (i==3 and j==6):
            print("*",end=" ")
        else :
             print(" ",end=" ")
    print()       
