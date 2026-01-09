import numpy as np
sales_report=np.array([
    [
        [10,11],
        [12,13]
    ],
    [
        [100,120],
        [120,130]
    ],

])
print(sales_report.ndim)#3
print(sales_report.shape)#(2, 2, 2)

print(sales_report[1,0,0])#100
print(sales_report[1,1,1])#130


#update
sales_report[0,1,1]=10
print(sales_report)#[[[ 10  11]
                   #[ 12  10]]

sales_report[1,1,1]=150
print(sales_report)#[[100 120]
                   #[120 150]]]
