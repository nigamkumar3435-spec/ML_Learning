# To Read Excel Data
import pandas as pd
ExcelData=pd.read_excel('Iris_data_sample.xlsx')
ExcelData

#...
ExcelData=pd.read_excel('Iris_data_sample.xlsx',sheet_name='Sheet1')
ExcelData
