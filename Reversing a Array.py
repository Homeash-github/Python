a = eval(input("Enter any Array : "))
t=type(a)
if t==type(list()):
    a.reverse()
    print("Reversed Array : ",a)
elif t==type(tuple()):
    a=list(a)
    a.reverse()
    print("Reversed Array : ",a)