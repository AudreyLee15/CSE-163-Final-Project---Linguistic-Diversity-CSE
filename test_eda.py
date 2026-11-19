import os
import pandas as pd
import os

#Read the datasets
data1 = pd.read_csv("Language Spoken At Home.csv")
data2 = pd.read_csv("Age by Language Spoken.csv")

data1["Label (Grouping)"] = data1["Label (Grouping)"].str.strip()
data2["Label (Grouping)"] = data2["Label (Grouping)"].str.strip()

# Converts Strings to Integers
cols = ["United States!!Estimate", "United States!!Margin of Error"]

data1[cols] = data1[cols].replace(r"[±,]", "", regex=True).astype(int)
data2[cols] = data2[cols].replace(r"[±,]", "", regex=True).astype(int)

joined_data = pd.merge(
    data1,
    data2,
    on="Label (Grouping)",
    how="outer",
    suffixes=("_Language", "_Age"),
)

combined_data = pd.concat(
    [
        data1.assign(Dataset="Language Spoken At Home"),
        data2.assign(Dataset="Age by Language Spoken"),
    ],
    ignore_index=True,
)

assert len(joined_data) > 0
assert len(combined_data) > 0

assert (combined_data.isna().sum().sum()) == 0

assert "Label (Grouping)" in joined_data.columns
assert "United States!!Estimate_Language" in joined_data.columns
assert "United States!!Margin of Error_Language" in joined_data.columns
assert "United States!!Estimate_Age" in joined_data.columns
assert "United States!!Margin of Error_Age" in joined_data.columns

assert "Label (Grouping)" in combined_data.columns
assert "United States!!Estimate" in combined_data.columns
assert "United States!!Margin of Error" in combined_data.columns
assert "Dataset" in combined_data.columns

for value in combined_data["United States!!Estimate"]:
    assert type(value) == int

for value in combined_data["United States!!Margin of Error"]:
    assert type(value) == int

assert os.path.exists("combined_bar_plot.png")
assert os.path.exists("combined_scatter_plot.png")

print("All tests pass!")
