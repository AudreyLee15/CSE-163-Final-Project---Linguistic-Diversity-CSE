import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data1 = pd.read_csv("Language Spoken At Home.csv")
data2 = pd.read_csv("Age by Language Spoken.csv")

#print(data1.isna().sum().sum())
#print(data2.isna().sum().sum())

#print(data1.columns)
#print(data2.columns)

# Converting Strings to Integers
cols = ["United States!!Estimate", "United States!!Margin of Error"]

data1[cols] = data1[cols].replace(r"[±,]", "", regex=True).astype(int)
data2[cols] = data2[cols].replace(r"[±,]", "", regex=True).astype(int)

cols = ["United States!!Estimate", "United States!!Margin of Error"]

data1[cols] = data1[cols].replace(r"[±,]", "", regex=True).astype(int)
data2[cols] = data2[cols].replace(r"[±,]", "", regex=True).astype(int)

# Join the datasets on Label
joined_data = pd.merge(
    data1,
    data2,
    on="Label (Grouping)",
    how="outer",
    suffixes=("_Language", "_Age"),
)

# Combined dataset across both tables
combined_data = pd.concat(
    [
        data1.assign(Dataset="Language Spoken At Home"),
        data2.assign(Dataset="Age by Language Spoken"),
    ],
    ignore_index=True,
)

combined_no_total = combined_data[
    ~combined_data["Label (Grouping)"].str.contains("Total", case=False, na=False)

# Bar Plot 1
plt.figure(figsize=(10, 6))
sns.barplot(
    data=data1[ # Excluding "Total" from the displayed estimate values
        ~data1["Label (Grouping)"].str.contains("Total", case=False, na=False)
    ],
    x="Label (Grouping)",
    y="United States!!Estimate",
    color="#2b5c8f",
    width=0.6,
    edgecolor="black",
)
plt.title("Languages Spoken at Home (Age 5+)")
plt.xlabel("Language Group")
plt.ylabel("Estimate")
plt.xticks(rotation=45, ha="right")
plt.ticklabel_format(style="plain", axis="y")
plt.savefig("bar_plot1.png", bbox_inches="tight")
plt.close()

# Bar Plot 2: Age Groups by Language Spoken
plt.figure(figsize=(10, 6))
sns.barplot(
    data=data2[ # Excluding "Total" from the displayed estimate values (again, lol)
        ~data2["Label (Grouping)"].str.contains("Total", case=False, na=False)
    ],
    x="Label (Grouping)",
    y="United States!!Estimate",
    color="#d95f02",
    width=0.6,
    edgecolor="black",
)
plt.title("Age Groups by Language Spoken at Home")
plt.xlabel("Age Group")
plt.ylabel("Estimate")
plt.xticks(rotation=45, ha="right")
plt.ticklabel_format(style="plain", axis="y")
plt.savefig("bar_plot2.png", bbox_inches="tight")
plt.close()

# Scatter Plot 1
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=data1,
    x="United States!!Estimate",
    y="United States!!Margin of Error",
    color="#2b5c8f",
    s=70,
    alpha=0.8,
)
plt.title("Language Estimates and Margin of Error")
plt.xlabel("Estimate")
plt.ylabel("Margin of Error")
plt.ticklabel_format(style="plain")
plt.xticks(rotation=30, ha="right")
plt.savefig("scatter_plot1.png", bbox_inches="tight")
plt.close()

# Scatter Plot 2
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=data2,
    x="United States!!Estimate",
    y="United States!!Margin of Error",
    color="#d95f02",
    s=70,
    alpha=0.8,
)
plt.title("Age Estimates and Margin of Error")
plt.xlabel("Estimate")
plt.ylabel("Margin of Error")
plt.ticklabel_format(style="plain")
plt.xticks(rotation=30, ha="right")
plt.savefig("scatter_plot2.png", bbox_inches="tight")
plt.close()