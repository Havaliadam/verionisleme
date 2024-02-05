#dağılım grafikleri
import seaborn as sns 
diamonds=sns.load_dataset("diamonds")
# ordinal tanımlama
from pandas.api.types import CategoricalDtype
df=diamonds.copy()
df.head()
print(df.info())
print(df.describe().T)

print(df["cut"].value_counts())


print(df["color"].value_counts())


#df.cut().head(1)


cut_kategoriler=["Fair","Good","Very Good","Premium","Ideal"]

df.cut.astype(CategoricalDtype(categories=cut_kategoriler,ordered=True))


#barplot 
print(df["cut"].value_counts().plot.barh().set_title("Cut değişken sınıf frekanslari"))


print(df["cut"].value_counts().plot.barh().set_title("Cut değişken sınıf frekanslari"))

sns.barplot(x="cut",y=df.cut.index,data=df)


