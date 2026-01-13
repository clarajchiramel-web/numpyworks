import numpy as np
data=np.genfromtxt("fileworks//titanic_casestudy//passenger.csv",delimiter=",",skip_header=1,filling_values=0,dtype="str")
#total numbers of passengers
print(data.shape)

#survival analysis
#total number of survivals
survived=data[data[:,1].astype("int")==1]
print(survived.shape)
#total number of death
un_survived=data[data[:,1].astype('int')==0]
print(un_survived.shape)
#survival rate
surived_unsurvived=data[:,1].astype("int")
survived=surived_unsurvived[surived_unsurvived==1]
print(survived.size)
surival_rate=(survived.size/surived_unsurvived.size)*100
print(surival_rate)
#unsurvival rate
survival_unsurival=data[:,1].astype("int")
unsurvival=survival_unsurival[survival_unsurival==0]
print(unsurvival.size)
unsurvival_rate=(unsurvival.size/survival_unsurival.size)*100
print(unsurvival_rate)


#gender analysis
#total number of males
total_males=data[data[:,3]=="male"]
print(total_males.shape)
#total number of females
total_females=data[data[:,3]=="female"]
print(total_females.shape)
#male survival rate
survived_males = data[(data[:, 3] == "male") &(data[:, 1].astype(int) == 1)]
male_count = survived_males[:,0].size
print(male_count)
#female survival rate
survived_female=data[(data[:,3]=="female") &(data[:,1].astype(int)==1)]
female_count=survived_female[:,0].size
print(female_count)

#age analysis(max,min,avg)
age=data[:,4].astype("int")
print(np.max(age))
print(np.min(age))
print(np.average(age))

#fare analysis(max,min,avg)
fare=data[:,5].astype("float")
print(np.max(fare))
print(np.min(fare))
print(np.average(fare))
#sort of fare
print(data[np.argsort(data[:,5].astype("float"))])




