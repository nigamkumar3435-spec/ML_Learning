#Calculate Total salary by Gender

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

plt.bar(gender, totalsal, color='green')  #gender vs total salary as a bar graph
