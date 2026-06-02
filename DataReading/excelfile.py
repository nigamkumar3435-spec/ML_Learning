# To Read Excel Data
import pandas as pd
ExcelData=pd.read_excel('Iris_data_sample.xlsx')
ExcelData

#...
ExcelData=pd.read_excel('Iris_data_sample.xlsx',sheet_name='Sheet1')
ExcelData

#To Read another Excel file
df_excel=pd.read_excel("Book1.xlsx")
df_excel

#delete a column
df_excel=df_excel.drop(columns=['Department'])
df_excel.head()
