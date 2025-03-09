import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.cm as cm

Creditcard_df = pd.read_csv('CreditcardData.csv')

print(Creditcard_df.head())

# Create a dashboard with subplots
fig, axes = plt.subplots(3, 2, figsize=(10, 8))
fig.suptitle("Credit Card Data Dashboard", fontsize=16, fontweight="bold")


# 1. plot the scatter plot to find the correlation between credit card limit
# and average purchase made on the card

sns.scatterplot(data=Creditcard_df, x="Credit_Limit", y="Avg_Purchase", hue="Income_Category",ax=axes[0, 0])
axes[0, 0].set_title("Credit Limit vs. Avg Purchase")
axes[0, 0].set_xlabel("Credit Limit")
axes[0, 0].set_ylabel("Avg Purchase")
axes[0, 0].legend(loc='upper left', prop={'size':8}, frameon=False)

# 2. Distribution plot for Credit Card Limit and Average Purchase

sns.kdeplot(Creditcard_df['Credit_Limit'], fill=True, color='blue', label='Credit Limit',ax=axes[0, 1])
sns.kdeplot(Creditcard_df['Avg_Purchase'], fill=True, color='darkblue', label='Avg_Purchase',ax=axes[0, 1])

axes[0, 1].set_title("Distribution of Credit Limit & Avg Purchase")
axes[0, 1].set_xlabel("Value")
axes[0, 1].set_ylabel("Density")
axes[0, 1].legend()

# Box plot for outliers in Credit Card Limit and Average Purchase

sns.boxplot(data=Creditcard_df[['Credit_Limit', 'Avg_Purchase']],ax=axes[1, 0])
axes[1, 0].set_title("Outlier in Credit Card Limit & Average Purchase")

# 3. plot the bar chart for Income Category

sns.countplot(data=Creditcard_df, x="Income_Category", hue="Income_Category", ax=axes[1, 1])
axes[1, 1].set_title("Income Category Distribution")
axes[1, 1].set_xlabel("Income Category")
axes[1, 1].set_ylabel("Number of Customers")
plt.tight_layout()

# 4. plot the Histogram for frequency distribution of the total transaction amount.

sns.histplot(Creditcard_df["Total_Trans_Amt"], bins=20, kde=True, color="Green", ax=axes[2, 0])
axes[2, 0].set_title("Total Transaction Amount Frequency")
axes[2, 0].set_xlabel("Total Transaction Amount")
axes[2, 0].set_ylabel("Frequency")

# 5. Plot Pie Chart for the percentage of customers retained and those attrition

cust_counts = Creditcard_df["Attrition_Flag"].value_counts()
labels = cust_counts.index
sizes = cust_counts.values

axes[2, 1].pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140, explode=(0,0.1), colors=['skyblue','lightblue'])
axes[2, 1].set_title("Customer Retention vs. Attrition")

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.96])

plt.show()
