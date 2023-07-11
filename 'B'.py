import time
for i in range (0,7):
    for j in range(0,5):
        if(i==0 and j in range(0,3))or(i==1 and j==0)or(i==1 and j-1==2)or(i==2 and j==0)or(i==2 and j-i==2)or(i==3 and j in range(0,4))or(i==4 and j==0)or(i==4 and i-j==1)or(i==5 and j==0)or(i==5 and i-j==1)or(i==6 and j in range (0,4)):
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
time.sleep(5)
print("aborting")
