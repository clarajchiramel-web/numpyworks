import numpy as np
#np.loadtext(file_path,delimeter=,skip_rows)
data=np.loadtxt("fileworks//sales_data//sales.csv",delimiter=",",skiprows=1,dtype="str")
print(data)

#sum 
units_sold=data[:,3].astype("int")
print(np.sum(units_sold),"total units sold") #79 total units sold

#max
max_unit_sold=data[:,3].astype("int")
print(np.max(max_unit_sold),"max units sold") #15 max units sold

#min
min_unit_sold=data[:,3].astype("int")
print(np.min(min_unit_sold),"min units sold") #3 min units sold

#avg
avg_unit_sold=data[:,3].astype("int")
print(np.average(avg_unit_sold),"avg units sold") #7.9 avg units sold

#revenue
revenue=data[:,3].astype("int")*data[:,4].astype("float")
print(revenue)#[275000. 240000. 210000.  35000.  32000. 315000. 168000.  28800.  49200.
#total 
print(np.sum(revenue))#1632000.0

#uits sold>8
print(data[data[:,3].astype("int")>8])

#catagory==electronics
print("electronics",data[data[:,2]=="Electronics"])

#discount 100 
data[:,4] = data[:,4].astype(int) - 100
print(data,"discount")

#total revenue of north region
north_region=data[data[:,-1]=="North"]
print(north_region)

revenue=north_region[:,3].astype("int")*north_region[:,4].astype("int")
print(np.sum(revenue))
