import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from google.colab import drive

drive.mount('/content/drive',force_remount=True)

data = pd.read_csv('/content/drive/MyDrive/ML_Lab/Toyota (1).csv', index_col=0, na_values=["??", "###", "????"])

print(data.head(10))

#Taking two independent variables- Age and KM

data['KM'].fillna(data['KM'].mean(), inplace=True)
data['Age'].fillna(data['Age'].mean(), inplace=True)

km=KMeans(n_clusters=3)
y_predicted=km.fit_predict(data[['Price','Age','KM']])
y_predicted

data['cluster']=y_predicted
data

#Plotting against KM

d1=data[data.cluster==0]
d2=data[data.cluster==1]
d3=data[data.cluster==2]

plt.scatter(d1.Price,d1['KM'],color='green')
plt.scatter(d2.Price,d2['KM'],color='red')
plt.scatter(d3.Price,d3['KM'],color='blue')

plt.xlabel('Price')
plt.ylabel('KM')
plt.legend()
