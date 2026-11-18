import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data1 = pd.read_csv("Language Spoken At Home.csv")
data2 = pd.read_csv("Age by Language Spoken.csv")

#print(data1.isna().sum().sum())
#print(data2.isna().sum().sum())

#print(data1.columns)
#print(data2.columns)

plt.figure()
sns.barplot(data=data1, x="Label (Grouping)",
            y="United States!!Estimate")

plt.title("Languages Spoken at Home (Age 5+)")
plt.xlabel("Language Group")
plt.ylabel("Estimate")
plt.savefig("bar_plot1.png")
plt.show()

plt.figure()
sns.barplot(data=data2, x="Label (Grouping)",
            y="United States!!Estimate")

plt.title("Age Groups by Language Spoken at Home")
plt.xlabel("Age Group")
plt.ylabel("Estimate")
plt.savefig("bar_plot2.png")
plt.show()

plt.figure()
sns.scatterplot(data=data1, x="United States!!Estimate",
                y="United States!!Margin of Error")

plt.title("Language Estimates and Margin of Error")
plt.xlabel("Estimate")
plt.ylabel("Margin of Error")
plt.savefig("scatter_plot1.png")
plt.show()

plt.figure()
sns.scatterplot(data=data2, x="United States!!Estimate",
                y="United States!!Margin of Error")

plt.title("Age Estimates and Margin of Error")
plt.xlabel("Estimate")
plt.ylabel("Margin of Error")
plt.savefig("scatter_plot2.png")
plt.show()