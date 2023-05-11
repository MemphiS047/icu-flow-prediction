# from scipy import stats

# # Outlier detection
# z_scores = stats.zscore(df)
# df_no_outliers = df[(z_scores < 3).all(axis=1)]


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('data/data-1683746571293.csv')

# Basic statistics
print(df.head())  # Display the first few rows
print(df.info())  # Summary of the dataset

# Descriptive statistics
print(df.describe())  # Statistical summary
print(df.corr())  # Correlation matrix

# Data visualization

# Pairwise relationships using scatter plots
sns.pairplot(df)
plt.show()

# Distribution of numerical features using histograms
df.hist(bins=20, figsize=(10, 8))
plt.tight_layout()
plt.show()

# Correlation heatmap
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()

# Box plots for numerical features
for col in df.select_dtypes(include='number'):
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, y=col)
    plt.ylabel(col)
    plt.show()

# Bar plots for categorical features
for col in df.select_dtypes(include='object'):
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x=col)
    plt.xlabel(col)
    plt.show()
