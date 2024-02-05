import seaborn as sns 
import pandas as pd 
planets=sns.load_dataset("planets")# veri kümesi
planets.head()

df=planets.copy()
df.method=pd.Categorical(df.method)

print(df.head())# ilk beş gözlem
# print(df.tail())# sondan 5 gözlem deperi
# print(df.info())#  kayıtözellikleri gösterir

