import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('ZappyLoanData.xlsx')

# Q1. Percentage of female applicants approved
female_df = df[df['Gender'] == 2]
f_apr = female_df[female_df['Loan_Status'] == 'Y']
f_per = (len(f_apr) / len(female_df)) * 100

print("Q1 Percentage of female applicants approved:", round(f_per, 2), "%")

# Q2. Average income of self-employed applicants
selfemployed_df = df[df['Self_Employed'] == 1]
s_avg = selfemployed_df['ApplicantIncome'].mean()

print("Q2 Average income of self-employed applicants:", round(s_avg, 2))

# Q3. Average income of graduate applicants
graduate_df = df[df['Graduate'] == 1]
g_avg = graduate_df['ApplicantIncome'].mean()

print("Q3 Average income of graduate applicants:", round(g_avg, 2))

# Q4. Percentage of graduate applicants approved
g_apr = graduate_df[graduate_df['Loan_Status'] == 'Y']
g_per = (len(g_apr) / len(graduate_df)) * 100

print("Q4 Percentage of graduate applicants approved:", round(g_per, 2), "%")

# Q5. Highest loan amount approved to male applicants
male_apr = df[(df['Gender'] == 1) & (df['Loan_Status'] == 'Y')]
highest_loan = male_apr['LoanAmount'].max()

print("Q5 Highest loan amount approved to male applicants:", highest_loan)

# Visualization
cats = [
    'Female Approval %',
    'Self-employed Avg Income',
    'Graduate Avg Income',
    'Graduate Approval %',
    'Highest Male Loan'
]

vals = [f_per, s_avg, g_avg, g_per, highest_loan]

plt.figure(figsize=(10, 6))
plt.bar(cats, vals)

plt.title('Zappy Loan Business Analysis')
plt.xlabel('Business Metrics')
plt.ylabel('Values')
plt.xticks(rotation=20)

plt.show()
