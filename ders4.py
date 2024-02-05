import seaborn as sns 
import pandas as pd 
planets=sns.load_dataset("planets")# veri kümesi
df=planets.copy()
planets.head()#ilk değer
# sadece kategorik değişken

kat_df=df.select_dtypes(include=["object"])
# print(kat_df.head(10))
# print(kat_df.tail(10))

#sınıf sayisina erişmek
print(kat_df.method.unique())
print(kat_df["method"].value_counts().count())# sayma işlemi
# sınıfların frekansları erişmek
print(kat_df["method"].value_counts())


df["method"].value_counts().plot.barh()