# from scipy import stats

# # Outlier detection
# z_scores = stats.zscore(df)
# df_no_outliers = df[(z_scores < 3).all(axis=1)]


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from preprocessing import connect_database, get_base_dataset

# Load the dataset
conn = connect_database()
cur = conn.cursor()
df = get_base_dataset(cur)

# Basic statistics
print(df.head())
print(df.info())

# Descriptive statistics
print(df.describe())
print(df.corr())

# Pairwise relationships using scatter plots
sns.pairplot(df)
plt.show()

# # Distribution of numerical features using histograms
# df.hist(bins=20, figsize=(10, 8))
# plt.tight_layout()
# plt.show()

# # Correlation heatmap
# sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
# plt.show()

# # Box plots for numerical features
# for col in df.select_dtypes(include='number'):
#     plt.figure(figsize=(8, 6))
#     sns.boxplot(data=df, y=col)
#     plt.ylabel(col)
#     plt.show()

# # Bar plots for categorical features
# for col in df.select_dtypes(include='object'):
#     plt.figure(figsize=(8, 6))
#     sns.countplot(data=df, x=col)
#     plt.xlabel(col)
#     plt.show()
