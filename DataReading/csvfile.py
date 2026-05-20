# To Read CSV data

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
