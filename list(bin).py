import pickle
l=9765321
f=open("list.txt","wb")
pickle.dump(l,f)
print("List added")
f.close()
