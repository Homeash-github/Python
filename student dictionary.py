d={}
l={}
j=True
grd=""
A=int(input("Enter number of Students : "))
for i in range(A):
    n=a=m=r=s=0
    print("Enter Student",i+1,end=" ")
    n=input(" Name : ")
    a=int(input("Enter  Class : " ))
    m=input("Enter Section : ")
    r=input("Enter Admin.No : ")
    d[n]={"Class":a,"Sec":m,"Admin.No":r} 
while j:
    g=int(input("""
Enter 1 to enter marks
Enter 2 to update details  
Enter 3 to update marks 
Enter 4 to display students details
Enter 5 to display students marks
Enter 6 to exit
"""))
    if g==2:
        z=input("Enter Student name : ")
        y=input("Enter the key which is to be updated : ")
        x=input("Enter the values for the key : ")
        if z in d.keys():
            d[z][y]=x
        print(d)
        print(l)
    elif g==1:
        for k in range(A):
            n=input("Enter student Name : ")
            p=int(input("Enter Physics marks :" ))
            c=int(input("Enter Chemistry marks :" ))
            s=int(input("Enter Computer marks :" ))
            h=int(input("Enter Maths marks :" ))
            e=int(input("Enter English marks :" ))
            tot=p+c+s+h+e
            avg=tot/5
            if (avg >85):
                grd="A"
            elif(avg<=85 and avg>70):
                grd="B"
            elif(avg<=70 and avg>55):
                grd="C"
            elif(avg<=55 and avg>40):
                grd="D"
            else:
                grd="E"
            l[n]={"Physic":p,"Chemistry":c,"Computer":s,"Maths":h,"English":e,"total":tot,"Average":avg,"Grade":grd}
        print(d)
        print(l)
    elif g==3:
        q=input("Enter Student name : ")
        w=input("Enter the subject which is to be updated : ")
        e=input("Enter the marks for the subject : ")
        if q in l.keys():
            l[q][w]=e  
        print(d)
        print(l)
    elif g==4 :
        print(d)
    elif g==5 :
        print(l)
    elif g==6 :
        j==False
        break
    else :
        print("Wrong input ! ! !")
    
