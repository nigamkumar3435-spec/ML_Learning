#step 1
import pandas as pd

#step 2
purchase=pd.read_csv('https://github.com/YBIFoundation/Dataset/raw/main/Customer%20Purchase.csv')
print(purchase.head())

purchase.info()

purchase.describe()

#step 3
purchase.columns

y=purchase['Purchased']
X=purchase.drop(['Purchased','Customer ID'],axis=1)
#encoding categorical variable
X.replace({'Review':{'Poor':0,'Average':1,'Good':2}},inplace=True)
X.replace({'Education':{'School':0,'UG':1,'PG':2}},inplace=True)
X.replace({'Gender':{'Female':0,'Male':1}},inplace=True)

#step 4: train test split
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.8, random_state=26)

#check shape of train and test sample
X_train.shape,X_test.shape,y_train.shape,y_test.shape

#step 5: select model
from sklearn import linear_model
model=linear_model.LogisticRegression()

#step 6:train or fit model
model.fit(X_train,y_train)

#RandomForest Classifier()

#step 7: predict model
y_pred=model.predict(X_test)
print(y_pred)

#step 8: model accuracy
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
print(y_test)
print(y_pred)
print(accuracy_score(y_test,y_pred))
print(confusion_matrix(y_test,y_pred))

print(classification_report(y_test,y_pred))
