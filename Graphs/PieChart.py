#Calculate salary distribution between males and females

import pandas as pd
import matplotlib.pyplot as plt
from google.colab import drive
drive.mount('/content/drive',force_remount=True)
data=pd.read_csv('/content/drive/MyDrive/ML_Lab/EMP1.csv')
data
gender=[]
totalsal=[]
gender.append('male')
ms=data[(data['Gender']==0)]['Salary'].sum()
totalsal.append(ms)

gender.append('female')
fs=data[(data['Gender']==1)]['Salary'].sum()
totalsal.append(fs)

c=['#ff9203','#029fff']
e=[0,1]
plt.pie(totalsal,labels=gender,colors=c)
plt.xlabel('Gender')
plt.ylabel('Total_Salary')
plt.title('Gender Vs Total Salary')  #show salary distribution between males and females using a pie chart.
