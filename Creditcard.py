import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.cm as cm

Creditcard_df = pd.read_csv('CreditcardData.csv')

print(Creditcard_df.head())

# 1. plot the scatter plot to find the correlation between credit card limit
# and average purchase made on the card
plt.figure(figsize=(8,5))
sns.scatterplot(data=Creditcard_df, x="Credit_Limit", y="Avg_Purchase", hue="Income_Category")
plt.title("Credit limit and Average purchase")
plt.xlabel('Credit card limit')
plt.ylabel('Average purchase')
#plt.show()

# 2. Distribution plot for Credit Card Limit and Average Purchase

plt.figure(figsize=(8,5))

sns.kdeplot(Creditcard_df['Credit_Limit'], fill=True, color='blue', label='Credit Limit')
sns.kdeplot(Creditcard_df['Avg_Purchase'], fill=True, color='darkblue', label='Avg_Purchase')

plt.title("Distribution of Credit Card Limit and Average Purchase")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
#plt.show()

# Box plot for outliers in Credit Card Limit and Average Purchase
plt.figure(figsize=(10, 6))
sns.boxplot(data=Creditcard_df[['Credit_Limit', 'Avg_Purchase']])
plt.title("Outlier Detection for Credit Card Limit and Average Purchase")
#plt.show()

# 3. plot the bar chart for Income Category

plt.figure(figsize=(8,5))

sns.countplot(data=Creditcard_df, x="Income_Category", hue="Income_Category")
plt.title("Number of Customers in each Income Category")
plt.xlabel("Income Category")
plt.ylabel("Number of Customers")
plt.tight_layout()

#plt.show()

# 4. plot the Histogram for frequency distribution of the total transaction amount.

plt.figure(figsize=(8,6))

sns.histplot(Creditcard_df["Total_Trans_Amt"], bins=20, kde=True, color="Green")
plt.title("frequency distribution of the total transaction amount")
plt.xlabel("Total Transaction Amount")
plt.ylabel("Frequency")

#plt.show()

# 5. Plot Pie Chart for the percentage of customers retained and those attrition

cust_counts = Creditcard_df["Attrition_Flag"].value_counts()
labels = cust_counts.index
sizes = cust_counts.values

plt.figure(figsize=(8,6))
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140, explode=(0,0.1), colors=['skyblue','lightblue'])
plt.title("the percentage of customers retained and those attrition")

plt.show()