import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



data = {
    'Product ID': ['A', 'B', 'C', 'D' , 'E', 'F', 'G'],
    'Product Name': ['Dell', 'HP', 'Apple ', 'Lenovo' , 'Asus', 'Acer', 'Microsoft'],
    'Sales qty': [150, 200, 300, 400, 500, 600, 700],
    'Price': [700, 800, 1200, 900, Nan, 500, 1500],
    'Revenue': [105000, 160000, 360000, 360000, 300000, 300000, 1050000]
}
# Convert to DataFrame
df = pd.DataFrame(data)
# Display the first few rows of the dataframe
print(df.head())
# Explore the structure of the dataset by checking the data types and any missing values.
print(df.info())
print(df.isnull().sum())
# Clean the dataset by either filling or dropping any missing values.
df = df.dropna()

#task 2
#Compute the basic statistics of the numerical columns (e.g., mean, median, standard deviation) using .describe()
print(df.describe())
#Perform groupings on a categorical column (e.g., group by 'Product Name') and calculate aggregate statistics (e.g., total sales quantity, average price).
grouped = df.groupby('Product Name').agg({'Sales qty': 'sum', 'Price': 'mean', 'Revenue': 'sum'})
print(grouped)
#Identify any patterns or interesting findings from your analysis.
print(df.corr())

#task 3
#
#Line chart showing trends over time (for example, a time-series of sales data).
plt.figure(figsize=(10, 6))
plt.plot(df['Product Name'], df['Sales qty'], marker='o')
plt.title('Sales Quantity by Product Name')
plt.xlabel('Product Name')
plt.ylabel('Sales Quantity')
plt.grid()  
plt.show()

#Bar chart showing the comparison of a numerical value across categories (e.g., average petal length per species).
plt.figure(figsize=(10, 6))
sns.barplot(x='Product Name', y='Sales qty', data=df)
plt.title('Sales Quantity by Product Name')
plt.xlabel('Product Name')
plt.ylabel('Sales Quantity')
plt.grid()
plt.show()

#Histogram of a numerical column to understand its distribution.
plt.figure(figsize=(10, 6))
sns.histplot(df['Sales qty'], bins=10, kde=True)
plt.title('Distribution of Sales Quantity')
plt.xlabel('Sales Quantity')
plt.ylabel('Frequency')
plt.grid()
plt.show()

#Scatter plot to visualize the relationship between two numerical columns (e.g., sepal length vs. petal length).
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Price', y='Revenue', data=df)
plt.title('Price vs Revenue')
plt.xlabel('Price')
plt.ylabel('Revenue')
plt.grid()
plt.show()

#Customize your plots with titles, labels for axes, and legends where necessary.
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Price', y='Revenue', hue='Product Name', data=df, s=100)
plt.title('Price vs Revenue by Product Name')
plt.xlabel('Price')
plt.ylabel('Revenue')
plt.grid()
plt.show()

