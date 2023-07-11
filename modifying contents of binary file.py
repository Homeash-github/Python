# Modifying contents of a binary file (Object level)
import pickle
File = open("Demo.dat",'wb')
Data = [1,2,"one","two"]
pickle.dump(Data,File)
Data = [3,4,"two","three"]
pickle.dump(Data,File)
Data = [5,6,"Five","Six"]
pickle.dump(Data,File)
File.close()
File = open("Demo.dat",'rb+')
Modify = input("Enter number that needs modification ")
NewValue = 10
Found = False
try:
  while(True):
    offset = File.tell()
    Data = pickle.load(File)
    print(Data[0],type(Data[0]),Modify,type(Modify))
    if (Data[0] ==int(Modify)):
      Found = True
      Data[0] = NewValue
      File.seek(offset,0)
      pickle.dump(Data,File)
      print("Modification is done")
except EOFError:
  File.close() 
  if (Found == False):
    print("Value not found in the file")
 
#display contents after modification
File = open("Demo.dat",'rb')
try:
  while(True):
    Data = pickle.load(File)
    print(Data)
except EOFError:
  File.close()
