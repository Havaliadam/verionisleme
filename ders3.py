import seaborn as sns 
import pandas as pd 
planets=sns.load_dataset("planets")# veri kümesi
df=planets.copy()
planets.head()#ilk beş değeri


#eksik değerleri gösterme


print(df.isnull().any())# hic eksik gözlem var mı 


print(df.isnull().sum())# kaçar değer var 

print(df["orbital_period"].fillna(0,inplace=True))# essik 0 değerlerini eklemek
print(df.isnull().sum())

print(df["orbital_period"].fillna(df.orbital_period.mean(),inplace=True))

print(df.isnull().sum())

print(df.fillna().sum())