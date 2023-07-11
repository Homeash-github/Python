org_cost=float(input("Enter original cost: "))
N_price=float(input("Enter Net price: "))
gst=(N_price-org_cost)*100/org_cost
print("GST = ",gst,end='%') 

