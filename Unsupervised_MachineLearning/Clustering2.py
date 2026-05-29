# Age vs Price
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from google.colab import drive

drive.mount('/content/drive', force_remount=True)

data=pd.read_csv('/content/drive/MyDrive/ML_Lab/Toyota (1).csv',index_col=0,na_values=["??","????","????"])

#data = pd.read_csv('./Toyota.csv')

data['KM'].fillna(data['KM'].mean(),inplace=True)
data['Age'].fillna(data['Age'].mean(),inplace=True)

km=KMeans(n_clusters=2)
y_predicted=km.fit_predict(data[['Price','Age']])
y_predicted

data['cluster']=y_predicted
data

d1=data[data.cluster==0]
d2=data[data.cluster==1]
d3=data[data.cluster==2]

plt.scatter(d1.Price,d1['Age'],color='green')
plt.scatter(d2.Price,d2['Age'],color='red')
plt.scatter(d3.Price,d3['Age'],color='blue')

plt.xlabel('Price')
plt.ylabel('Age')
plt.legend()
