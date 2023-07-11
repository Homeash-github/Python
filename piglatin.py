a=input("Enter a word : ")
l=len(a)
for i in range(l):
    if a[i]=='A' or a[i]=='E' or a[i]=='I' or a[i]=='O' or a[i]=='U' or a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u':
        b=a[i+1:]+a[:i+1]+"AY"
        break
print(b)
