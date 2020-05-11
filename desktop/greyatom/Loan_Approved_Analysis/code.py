# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here

#Task -1 
#Let's check which variable is categorical and which one is numerical so that you will get a #basic idea about the features of the bank dataset.

categorical_var=bank_data.select_dtypes(include='object')
print(categorical_var.shape)

numerical_var=bank_data.select_dtypes(include='number')
print(numerical_var.shape)


#Task-2
banks=bank_data.drop(['Loan_ID'],axis=1)


print(banks.isnull().sum())


bank_mode=banks.mode()
print(bank_mode)


for column in banks.columns:
    banks[column].fillna(banks[column].mode()[0], inplace=True)


print(banks.isnull().sum())


#Task 3
#Now let's check the loan amount of an average person based on 'Gender', 'Married', #'Self_Employed'. This will give a basic idea of the average loan amount of a person.


avg_loan_amount=pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values=['LoanAmount'],aggfunc='mean')

print(avg_loan_amount)

#Task 4
#Now let's check the percentage of loan approved based on a person's employment type.

loan_approved_se = banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')]['Self_Employed'].count()
print(loan_approved_se)


loan_approved_nse = banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')]['Self_Employed'].count()
print(loan_approved_nse)

print(banks['Loan_Status'].count())

#percentage of loan approval for self-employed people and store result in variable 'percentage_se'.

percentage_se=(loan_approved_se/banks['Loan_Status'].count())*100
print(percentage_se)

#percentage of loan approval for people who are not self-employed and store the result in variable 'percentage_nse'.

percentage_nse=(loan_approved_nse/banks['Loan_Status'].count())*100
print(percentage_nse)

#Task - 5

#A government audit is happening real soon! So the company wants to find out those applicants with long loan amount term.


loan_term=banks['Loan_Amount_Term'].apply(lambda x: x/12)

big_loan_term=len(banks[loan_term>=25])
print(big_loan_term)

#Task -6 

#Now let's check the average income of an applicant and the average loan given to a person based on their income.

loan_groupby=banks.groupby('Loan_Status')[['ApplicantIncome','Credit_History']]
print(loan_groupby)

mean_values=loan_groupby.mean()
print(mean_values)












