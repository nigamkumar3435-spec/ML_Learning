#Code for qualification_salary_analysis

import pandas as pd
import matplotlib.pyplot as plt
from google.colab import drive
drive.mount('/content/drive',force_remount=True)
data=pd.read_csv('/content/drive/MyDrive/ML_Lab/EMP1.csv')
quali=['Undergraduate','Graduate','Postgraduate']

totalsal=[]

ug=data[(data['Qualification']==0)]['Salary'].sum()
totalsal.append(ug)

g=data[(data['Qualification']==1)]['Salary'].sum()
totalsal.append(g)

pg=data[(data['Qualification']==2)]['Salary'].sum()
totalsal.append(pg)

c=['cyan','skyblue','#9874ff']

plt.pie(totalsal,labels=quali,colors=c) #Displays the salary distribution according to qualification level using pie chart.
