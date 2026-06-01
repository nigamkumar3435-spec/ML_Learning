import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

#from sklearn.datasets import load_iris
purchase=pd.read_csv('https://github.com/YBIFoundation/Dataset/raw/main/Customer%20Purchase.csv')
X=purchase.drop(['Purchased','Customer ID'],axis=1)

#encoding categorical variable
X.replace({'Review':{'Poor':0,'Average':1,'Good':2}},inplace=True)
X.replace({'Education':{'School':0,'UG':1,'PG':2}},inplace=True)
X.replace({'Gender':{'Female':1,'Male':0}},inplace=True)
y=purchase['Purchased']

#split into train and test sets
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=10)

#feature scaling (important for KNN)
scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)

#Initialize and train KNN model
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_scaled,y_train)

#Predict on test date
y_pred=knn.predict(X_test_scaled)

#Actual Values
print(y_test)

#Predicted Values
print(y_pred)

#Evaluate the model
accuracy=accuracy_score(y_test,y_pred)
print(f"Accuracy: {accuracy:.2f}")

print("\nClassification Report:")
print(classification_report(y_test,y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test,y_pred))

#######
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

#from sklearn.datasets import load_iris
purchase=pd.read_csv('heart.csv',sep='\t')
print(purchase)
