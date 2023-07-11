def FindOut(Names,HisName):
    for i in range(len(Names)):
        if HisName == Names[i] :
            print(HisName,'at',i)
FindOut(["Arun","Raj","Tarun","Kanika"],"Tarun")
