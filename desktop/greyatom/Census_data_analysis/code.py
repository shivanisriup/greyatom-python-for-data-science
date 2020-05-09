# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#print(data)

#Code starts here

#Task -1 : In this first task, we will load the data to a numpy array and add a new record to it.

census=np.concatenate((data,new_record))

print(census.shape)

age=census[:,0].astype('int32')
print(age)

#Task -2 We often associate the potential of a country based on the age distribution of the people residing there. We too want to do a simple analysis of the age distribution

max_age=np.max(age)
min_age=np.min(age)
age_mean=age.mean()
age_std=np.std(age)

print(max_age)
print(min_age)
print(age_mean)
print(age_std)

#Task -3  The constitution of the country tries it's best to ensure that people of all races are able to live harmoniously. Let's check the country's race distribution to identify the minorities so that the government can help them.

race_0=np.array([census for census in census[:,2] if census == 0])
race_1=np.array([census for census in census[:,2] if census == 1])
race_2=np.array([census for census in census[:,2] if census == 2])
race_3=np.array([census for census in census[:,2] if census == 3])
race_4=np.array([census for census in census[:,2] if census == 4])

len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

min_race=np.min([len_0,len_1,len_2,len_3,len_4])

if len_0==min_race:
    minority_race=0
elif len_1==min_race:
    minority_race=1
elif len_2==min_race:
    minority_race=2
elif len_3==min_race:
    minority_race=3
elif len_4==min_race:
    minority_race=4

print(minority_race)

# Task - 4   As per the new govt. policy, all citizens above age 60 should not be made to work more than 25 hours per week. Let us look at the data and see if that policy is followed.

senior_citizens=[i for i in census.astype('int32') if i[0]>60]
senior_citizens_len=len(senior_citizens)
print(senior_citizens_len)

#working_hours_sum=[j.size for i,j in zip(senior_citizens,census[:,6].astype('int32'))]
#print(working_hours_sum)
working_hours_sum=0
for i in senior_citizens:
        working_hours_sum+=i[6]
print(working_hours_sum)



avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)


#Task -6 Our parents have repeatedly told us that we need to study well in order to get a good(read: higher-paying) job. Let's see whether the higher educated people have better pay in general.

high=np.array([i for i in census.astype('int32') if i[1]>10])


low=np.array([i for i in census.astype('int32') if i[1]<=10])


sum=0
for i in high[:,7]:
    sum+=i
avg_pay_high=(sum/len(high))
print(round(avg_pay_high,2))


sum=0
for i in low[:,7]:
    sum+=i
avg_pay_low=(sum/len(low))
print(round(avg_pay_low,2))





