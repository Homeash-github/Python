a=input("Enter a sentence : ")
b=a.upper()
b=" "+b
l=len (b)
count=0
for i in range(40):
    if b[i]==b[i+1]:
        count+=1
print("The frequency of double letter in the sentence : ",count)
