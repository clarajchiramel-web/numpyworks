import numpy as np

prices=np.array([100,120,130,140,150])
discount_prices=prices-10
print(discount_prices)#[ 90 110 120 130 140]

new_price=prices+10
print(new_price)#[110 130 140 150 160]

arr1=np.array([
    [1,2],
    [3,4]
])
arr2=np.array([
    [10,11],
    [12,13]
])
print(arr1+arr2)#[[11 13]
                #[15 17]]