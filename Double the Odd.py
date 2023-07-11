def DoubletheOdd():
    A=eval(input("Enter an Array : "))
    l=len(A)
    s=0
    for i in range(l):
        if A[i]%2 != 0:
            s+=A[i]
    s*=2    
    print('Twice of odd Sum : ',s)
DoubletheOdd()
