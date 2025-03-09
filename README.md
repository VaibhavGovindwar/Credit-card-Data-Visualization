# Credit-card-Data-Visualization

This project visualizes Credit Card Data using Python's matplotlib and seaborn libraries. The dashboard includes multiple plots to analyze credit card transactions, customer categories, and spending patterns.

## Visualizations

1. **Bivariate Plot: Credit Card Limit vs. Average Purchase**
   - **Type**: Scatter Plot
   - **Purpose**: Visualize the relationship between credit card limit and average purchase.
   - **Insight**: Identify potential correlations between these two variables.

2. **Distribution of Credit Card Limit and Average Purchase**
   - **Type**: Histogram and Box Plot
   - **Purpose**: 
     - Histograms to show the frequency distribution of credit limits and average purchases.
     - Box plots to identify outliers and data spread.
   - **Insight**: Understand data distribution and spot anomalies.

3. **Number of Customers in Each Income Group**
   - **Type**: Bar Chart
   - **Purpose**: Visualize the distribution of customers across different income groups.
   - **Insight**: Identify income group segments and their relative sizes.

4. **Frequency Distribution of Total Transaction Amount**
   - **Type**: Histogram
   - **Purpose**: Show the frequency of different total transaction amounts.
   - **Insight**: Understand how transaction amounts vary across customers.

5. **Customer Retention and Attrition**
   - **Type**: Pie Chart with Exploded Slice
   - **Purpose**: Show the proportion of retained and attrited customers.
   - **Insight**: Highlight attrition rates and emphasize customer churn.

---

## Dataset

The dataset used is CreditcardData.csv, which contains:

1️⃣ Credit_Limit - Maximum spending limit on the credit card

2️⃣ Avg_Purchase - Average purchase made on the card

3️⃣ Income_Category - Customer's income classification

4️⃣ Total_Trans_Amt - Total transaction amount

5️⃣ Attrition_Flag - Indicator if a customer is retained or attrited

### Prerequisites

Ensure you have the following installed:
- Python 3.10
- Required libraries:
  ```bash
  pip install pandas matplotlib seaborn pyplot
  ```

Running the Scripts
Clone the repository:

  ```bash
git clone https://github.com/VaibhavGovindwar/Credit-card-Data-Visualization.git
cd Credit-card-Data-Visualization
```

Run the scripts:

To generate visualizations, run each script:
  ```bash
python Creditcard.py
```

Example Outputs

![Figure_1](https://github.com/user-attachments/assets/a447aee2-8e0f-42af-94d7-47d5a812543a)


## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for improvements or additional visualizations.

Note: I took a course on Infosys Springboard and worked on this project there.

## License
This project is licensed under the MIT License.

Happy Coding! 🚀
