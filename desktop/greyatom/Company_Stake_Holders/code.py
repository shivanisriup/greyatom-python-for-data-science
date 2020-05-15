# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here

# Step 1 
#Reading the file

#print(data.head())

#Creating a new variable to store the value counts

loan_status=data['Loan_Status'].value_counts()

#Plotting bar plot

loan_status.plot(kind='bar')
plt.show()

# Step 2

#Company has more 'loan approvals' or 'loan disapprovals'?
#Can one of the company's health factors be its loan status distribution?

#Plotting an unstacked bar plot

property_and_loan=data.groupby(['Property_Area','Loan_Status'])
property_and_loan=property_and_loan.size().unstack()
property_and_loan.plot(kind='bar',stacked = False,figsize=(15,10))

#Changing the x-axis label

plt.xlabel('Property Area')

#Changing the y-axis label

plt.ylabel('Loan Status')

#Rotating the ticks of X-axis

plt.xticks(rotation=45)
plt.show()

# Step 3

#Which is the region with the highest no. of loan approvals? lowest no. of loan approvals?
#Which is the region with the maximum difference between loan approvals and loan rejections?

#Higher education has always been an expensive endeavour for people but it results in better #career opportunities and stability in life. But does higher education result in a better #guarantee in issuing loans?   

#Plotting a stacked bar plot
education_and_loan=data.groupby(['Education','Loan_Status'])
education_and_loan=education_and_loan.size().unstack()
education_and_loan.plot(kind='bar',stacked = False,figsize=(15,10))

#Changing the x-axis label

plt.xlabel('Education Status')

#Changing the y-axis label

plt.ylabel('Loan Status')

#Rotating the ticks of X-axis

plt.xticks(rotation=45)
plt.show()

# Step 4 

#After seeing the loan status distribution, let's check whether being graduate or not also #leads to different loan amount distribution by plotting an overlapping density plot of two #values

#Subsetting the dataframe based on 'Education' column

graduate=data[data['Education']=='Graduate']

#Subsetting the dataframe based on 'Education' column

not_graduate=data[data['Education']=='Not Graduate']

#Plotting density plot for 'Graduate'

graduate.plot(kind='density',label='Graduate')

#Plotting density plot for 'Not Graduate'

not_graduate.plot(kind='density',label='Not Graduate')

#For automatic legend display

plt.legend()
plt.show()

# Step 5

#For any financial institution to be successful in its loan lending system, there has to be a #correlation between the borrower's income and loan amount he is lent. Let's see how our #company fares in that respect:

#Setting up the subplots


fig,(ax_1,ax_2,ax_3)=plt.subplots(nrows=3,ncols=1,figsize=(20,10))

#Plotting scatter plot
#res.plot(kind='bar', stacked=True, ax=ax_1)
plt.scatter(data['ApplicantIncome'],data['LoanAmount'])

#Setting the subplot axis title

ax_1.set_title('Applicant Income')

#Plotting scatter plot

plt.scatter(data['CoapplicantIncome'],data['LoanAmount'])

#Setting the subplot axis title

ax_2.set_title('Coapplicant Income')

#Creating a new column 'TotalIncome'

data['TotalIncome']=data['CoapplicantIncome']+data['ApplicantIncome']

#Plotting scatter plot

plt.scatter(data['TotalIncome'],data['LoanAmount'])

#Setting the subplot axis title

ax_3.set_title('Total Income')


