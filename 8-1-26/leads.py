import numpy as np
leads = np.array([
    # s  m    t  w   th
    [12, 18, 10, 15, 5],   # facebook
    [20, 25, 22, 18, 8],   # insta
    [18, 30, 25, 22, 10],  # youtube
    [25, 28, 30, 26, 12],  # refferal
    [30, 35, 28, 32, 15],  # walkin
    [40, 45, 38, 40, 20],  # reddit
    [35, 50, 42, 45, 25]   # camp
])

arr=np.array(leads)
print(arr)

#total leads generated each day
print(np.sum(arr,axis=0)) #[180 231 195 198  95]

#total leads from each source 
print(np.sum(arr,axis=1)) #[60  93 105 121 140 183 197]

#hghest lead day
day_wise_total=np.sum(arr,axis=0)
max_total=np.max(day_wise_total)
print(np.argmax(day_wise_total)) #argmax is used to identigy the highest lead index #1

#average leads per source
print(np.average(arr,axis=1)) #[12.  18.6 21.  24.2 28.  36.6 39.4]

#average leads per day
print(np.average(arr,axis=0)) #[25.71428571 33. 27.85714286 28.28571429 13.57142857]

#highest lead source
highest_source=np.sum(arr,axis=1)
max_total=np.max(highest_source)
print(np.argmax(highest_source)) #6


