for i in range(0,6):
    for j in range(0,5):
        if  (i==0  and  j in range(0,2)) or  (i==1 and j%3 ==0) or (i==2 and j==0) or (i==2 and j==4) or (i==3 and j==0) or(i==3 and j==4) or (i==4 and j %3 ==0) or(i==5 and j in range(0,2)):
            print("*",end=" ")
        else :
             print(" ",end=" ")
    print()       
