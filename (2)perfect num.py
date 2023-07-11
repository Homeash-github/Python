N=int(input("Enter a number : "))
S=0
for i in range(1,N):
    if N%i == 0:
        S+=i
if S == N:
    print(N,"is a perfect number ")
else :
    print(N,"is not a perfect number ")
    
