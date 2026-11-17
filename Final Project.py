import pandas as pd

data1 = pd.read_csv("Language Spoken At Home.csv")
data2 = pd.read_csv("Age by Language Spoken.csv")

print(data1.isna().sum().sum())
print(data2.isna().sum().sum())