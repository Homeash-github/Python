str1=eval(input("Enter a alphanum: "));
l=len(str1);
sl=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];
nl=['0','1','2','3','4','5','6','7','8','9'];
S=[];
L=[]
for i in range(26):
    if sl[i] not in str1:
        S.append(sl[i]);
S.sort();
for i in range(10):
    if nl[i] not in str1:
        L.append(nl[i]);
L.sort();
L+=S;
print("Remaining aplhafnum:",(" ".join(L)))
print()
