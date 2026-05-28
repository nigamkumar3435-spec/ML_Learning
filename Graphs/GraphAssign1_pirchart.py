import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('ZappyLoanData.xlsx')

female_df = df[df['Gender'] == 2]
f_yes = female_df[female_df['Loan_Status'] == 'Y']

yes1 = len(f_yes)
no1 = len(female_df) - yes1

graduate_df = df[df['Graduate'] == 1]
g_yes = graduate_df[graduate_df['Loan_Status'] == 'Y']

yes2 = len(g_yes)
no2 = len(graduate_df) - yes2

plt.figure(figsize=(6,6))
plt.pie(
    [yes1, no1],
    labels=['Approved', 'Not Approved'],
    autopct='%1.1f%%'
)
plt.title('Female Loan Approval')
plt.show()

plt.figure(figsize=(6,6))
plt.pie(
    [yes2, no2],
    labels=['Approved', 'Not Approved'],
    autopct='%1.1f%%'
)
plt.title('Graduate Loan Approval')
plt.show()

