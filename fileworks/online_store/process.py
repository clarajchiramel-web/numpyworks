import numpy as np
data=np.loadtxt("fileworks/online_store/online.csv",delimiter=",",skiprows=1,dtype="str")
print(data)
#Load the CSV and display shape
print(data.shape,"shape of data")

#Calculate total number of orders
total_numbers=data[:,0].astype("int")
sum_numbers=np.sum(total_numbers)
print(sum_numbers,"total numbers orderd")

#Find average unit price
unit_price=data[:,6].astype("float")
average_unit=np.average(unit_price)
print(average_unit,"average of unit price")

#Calculate total revenue per order
revenue=data[:,0].astype("int")*data[:,6].astype("float")
total_revenue=np.sum(revenue)

#Find orders with delivery days > 5


#Count returned vs non-returned orders
status=data[:,-1].astype("int")
orders=np.where(status==0,"Returned","non Returned")
print(orders)

#Find average discount per product category
discounts = data[:, 2].astype(int)
avg_discount = np.average(discounts)
print("Average discount:", avg_discount)

#Create a new column:
#DeliveryDays ≤ 3 → Fast
#Else → Normal
delivery_days=data[:,7].astype("int")
print(np.where(delivery_days<=3,"fast","normal"))


