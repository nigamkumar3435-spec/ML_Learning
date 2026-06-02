# 1. To Read CSV data

import pandas as pd
CSVData=pd.read_csv('Iris_data_sample.csv',na_values=('??','###'))
# print(CSVData['SepalLengthCm'].dtype)
# print(CSVData.duplicated().sum())
# print(CSVData.isna().sum())
print(CSVData.head(6))
CSVData['SepalLengthCm']=CSVData['SepalLengthCm'].fillna(CSVData['SepalLengthCm'].mean())
CSVData['SepalWidthCm']=CSVData['SepalWidthCm'].fillna(CSVData['SepalWidthCm'].mean())
CSVData['PetalLengthCm']=CSVData['PetalLengthCm'].fillna(CSVData['PetalLengthCm'].mean())
print(CSVData.head(6))

#1. To read the Text data and CSV data
df_text=pd.read_csv("countries of the world.txt",sep='/t')
print(df_text)

df_csv=pd.read_csv("https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv")
df_csv
