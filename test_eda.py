import pandas as pd

data1 = pd.read_csv("Language Spoken At Home.csv")
data2 = pd.read_csv("Age by Language Spoken.csv")

assert data1 is not None
assert data2 is not None

assert len(data1) > 0
assert len(data2) > 0

assert (data1.isna().sum().sum()) == 0
assert (data2.isna().sum().sum()) == 0


assert "Label (Grouping)" in data1.columns
assert "United States!!Estimate" in data1.columns

assert "Label (Grouping)" in data2.columns
assert "United States!!Estimate" in data2.columns