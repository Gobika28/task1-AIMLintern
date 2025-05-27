import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv(r'C:\Users\gobik\OneDrive\Documents\task1data.csv')

print(df.head())
print("Basic Info:")
print(df.info())
print("Missing Values:")
print(df.isnull().sum())
print("Handling Missing Values.....")
df['Age']=df['Age'].fillna(df['Age'].mean())
df['Embarked']=df['Embarked'].fillna(df['Embarked'].mode()[0])
df.drop(['Cabin'],axis=1,inplace=True)
print("Missing Values after Cleaning:")
print(df.isnull().sum())
df.drop(columns=['Survived','Pclass','SibSp','Parch','Name'],inplace=True)
print("Encoding Categorical Columns....")
df['Sex']=df['Sex'].map({'male':0,'female':1})
print("After encoded the Columns:\n",df)

from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()
df[['Age','Fare']]=scaler.fit_transform(df[['Age','Fare']])
print("After standardization:\n",df)
sns.violinplot(x=df['Age'])
plt.show()

Q1=df['Age'].quantile(0.25)
Q2=df['Age'].quantile(0.75)
IQR=Q2-Q1
df=df[(df['Age']>=Q1-1.5*IQR)&(df['Age']<=Q2+1.5*IQR)]
print("Final Cleaned data:\n",df)