import csv
file=open("Student.csv","w+")
d=["Product code","product name","product price"]
wo=csv.writer(file)
wo.writerow(d)
while True:
    dr=input("Enter code,name,price").split()
    wo.writerow(dr)
    cont=input("Continue (y/n)")
    if cont =='n':
        file.close()
        break
file=open("Student.csv","w+")
r=csv.reader(file)
for row in r:
    print(row[0],row[2],row[3])
print(r)
file.close()
