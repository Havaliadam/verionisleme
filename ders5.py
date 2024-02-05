import seaborn as sns 
planets=sns.load_dataset("planets")# veri kümesi
df=planets.copy()
df.head()

df_num=df.select_dtypes(include=["float64","int64"])


print(df_num.head())


print(df_num.describe().T)


print(df_num["distance"].describe())


print("ortalama:"+str(df_num["distance"].mean()))
print("dolu gözlem sayisi:"+str(df_num["distance"].count()))
print("maksimun değer:"+str(df_num["distance"].mean()))
print("minumun değeri:"+str(df_num["distance"].min()))
print("medyan:"+str(df_num["distance"].median()))
print("standart sapma:"+str(df_num["distance"].std()))