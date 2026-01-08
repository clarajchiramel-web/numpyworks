import numpy as np

productivity = np.array([
    [8, 7, 8, 6, 7, 8, 9, 8, 7, 8],
    [6, 7, 6, 7, 6, 7, 8, 7, 6, 7],
    [9, 8, 9, 8, 9, 9, 8, 9, 8, 9],
    [5, 6, 5, 6, 5, 6, 6, 5, 6, 5],
    [7, 8, 7, 8, 7, 8, 7, 8, 7, 8],
    [8, 9, 8, 9, 8, 9, 8, 9, 8, 9]
])
arr=np.array(productivity)
print(arr)
#Calculate the total number of hours worked by each employee over 10 days.
print(np.sum(arr,axis=0))

# Calculate the total work hours for each day across all employees.
print(np.sum(arr, axis=0))

#4. Find the average working hours per day.
print(np.average(arr,axis=0))

#5. Identify the employee index who worked the maximum total hours.
max_total_hours=np.sum(arr,axis=1)
max_total=np.max(max_total_hours)
print(np.argmax(max_total_hours))

#6. Identify the employee index who worked the minimum total hours.
min_total_hours=np.sum(arr,axis=1)
min_total=np.min(min_total_hours)
print(np.argmin(min_total_hours))

#7. Find the day index with the highest total working hours.
highest_working_hour=np.sum(arr,axis=0)
highest_total=np.max(highest_working_hour)
print(np.argmax(highest_working_hour))

#8. Identify employees who are overworked if average hours exceed 8 per day.
avg_hours = np.average(arr, axis=1)
print(avg_hours)

#9. Calculate the difference between the most productive and least productive employee.
total_hours = np.sum(arr, axis=1)
print(total_hours)
