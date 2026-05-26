import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("/content/titanic_data.csv")

# first few rows
display(df.head)

# dataset shape
display(df.shape)

# column names & data types
df.info()

# generate basic stats
df.describe()

# identify categorical columns
df.select_dtypes(include=['object']).columns

# identiy missing values
df.isnull().sum()

# visualize missing data
sns.heatmap(df.isnull(), cbar=False)
plt.show()

# filling of missing data
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# checking for dupes
df.duplicated().sum()

# removing of dupes
df = df.drop_duplicates()

# plot distribution of a numerical feature
sns.histplot(df['Age'], bins=30, kde=True)
plt.show()

# plot count of a categorical feature
sns.countplot(x='Sex', data=df)
plt.show()
