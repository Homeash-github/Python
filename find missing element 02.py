arr = list(map(int,input().split(" ")))
l=len(arr)
n=l+1
sum_n=(n*(n+1))/2
sum_arr=sum(arr)
x=int(sum_n-sum_arr)
print("Missing Value : ",x)