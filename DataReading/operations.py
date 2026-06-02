#Some Basic Operations on csv file

df_iris=pd.read_csv("/content/Iris.csv")
print(df_csv)

#Mean
print(df_iris.mean(numeric_only=True))

#Median
print(df_iris.median(numeric_only=True))

#Mode
print(df_iris.mode(numeric_only=True))

#count of non-null values
print(df_iris.count())

#Species
print(df_iris['Species'].value_counts())
