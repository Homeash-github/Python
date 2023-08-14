n1 = int(input("Enter A: "))
n2 = int(input("Enter second n: "))
if n1 > n2:
  big = n1
else:
  big = n2
while(True):
  if((big % n1 == 0) and (big % n2 == 0)):
      lcm = big
      break
  big += 1
print("LCM: ",big)