import pandas as pd
import os

#Read the datasets
data1 = pd.read_csv("Language Spoken At Home.csv")
data2 = pd.read_csv("Age by Language Spoken.csv")

#Converts Strings to Integers
cols = ["United States!!Estimate", "United States!!Margin of Error"]

data1[cols] = data1[cols].replace(r"[±,]", "", regex=True).astype(int)
data2[cols] = data2[cols].replace(r"[±,]", "", regex=True).astype(int)

#Check that both datasets contain data
assert len(data1) > 0
assert len(data2) > 0

#Checking to make sure there aren't any missing values
assert (data1.isna().sum().sum()) == 0
assert (data2.isna().sum().sum()) == 0

#Check that the expected columns exist
assert "Label (Grouping)" in data1.columns
assert "United States!!Estimate" in data1.columns
assert "United States!!Margin of Error" in data1.columns

assert "Label (Grouping)" in data2.columns
assert "United States!!Estimate" in data2.columns
assert "United States!!Margin of Error" in data2.columns

#Check that numerical columns were converted to integers
for value in data1["United States!!Estimate"]:
    assert type(value) == int

for value in data2["United States!!Estimate"]:
    assert type(value) == int

for value in data1["United States!!Margin of Error"]:
    assert type(value) == int

for value in data2["United States!!Margin of Error"]:
    assert type(value) == int

#Check that all four graphs were saved
assert os.path.exists("bar_plot1.png")
assert os.path.exists("bar_plot2.png")
assert os.path.exists("scatter_plot1.png")
assert os.path.exists("scatter_plot2.png")

print("All tests pass!")
