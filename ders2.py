import seaborn as sns 
import pandas as pd 
planets=sns.load_dataset("planets")# veri kümesi
# planets.head()#ilk beş değeri

df=planets.copy()
# df.method=pd.Categorical(df.method)

#df.shape()#kaç satır kaç sütün oldugu gösteriri

# print(df.columns())# index değerleri
print(df.describe().T)#oranlarına göre göstri

