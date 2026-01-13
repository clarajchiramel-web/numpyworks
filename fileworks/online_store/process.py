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
orders=data[data[:,5].astype("int")>5]
print(orders)

#Count returned vs non-returned orders
returned=data[data[:,-1]=="Yes"]
non_returned=data[data[:,-1]=="No"]
print("returned=",len(returned),"non returned=",len(non_returned))

#Find average discount per product category
print(np.average(data[:,3:7].astype("int")))

#Create a new column:
#DeliveryDays ≤ 3 → Fast
#Else → Normal
