import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/drive', force_remount=True)
data=pd.read_excel('/content/drive/MyDrive/ML_Lab/EMP.xlsx')

print(data)

linreg=linear_model.LinearRegression()
linreg.fit(data[['Experience']],data[['Salary']])
print(linreg.coef_)
print(linreg.intercept_)
p=linreg.predict([[8]])
print(p)
data.loc[3,'Experience']=8
data.loc[3,'Salary']=p[0][0]

#fig, axes = plt.subplots(1,3, figsize=(10,5))
print(data)
plt.scatter(data['Experience'], data['Salary'])
# plt.set_title('Experience vs Salary')
# plt.set_xlabel('Experience')
# plt.set_ylabel('Salary')
plt.plot(data['Experience'],linreg.predict(data[['Experience']]),color='blue')
# plt.tight_layout()
plt.show()
