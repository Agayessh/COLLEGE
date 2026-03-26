import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

# import
gold_data = pd.read_csv("/content/gld_price_data.csv")

gold_data.head() # 1st 5 rows of the data frame
gold_data.tail() # last rows
gold_data.describe() # statistical measures of the data
gold_data.shape # number & columns
gold_data.info() # data types

# check missing values
gold_data.isnull().sum()

correlation = gold_data.drop('Date', axis=1).corr()
plt.figure(figsize=(8,8))
sns.heatmap(
      correlation, cbar=True, square=True, annot=True, annot_kws={'size': 8}, cmap='Blues')

# correlation values of Gold
print(correlation['GLD'])

# checking the distribution of the gold prices
sns.distplot(gold_data['GLD'], color='blue')

# split data into 2 types (Features & Target)
X = gold_data.drop(['Date', 'GLD'], axis=1)
y = gold_data['GLD']

print(X)
print(y)

# training
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.1, random_state=1)

regressor = RandomForestRegressor(n_estimators=100)
regressor.fit(X_train,y_train, sample_weight=None) # training

# prediction
test_data_prediction = regressor.predict(X_test)
print(test_data_prediction)

# R^2 error
error_score = metrics.r2_score(y_test, test_data_prediction)
print(f'R-Squared Error: {error_score}')
y_test = list(y_test)

plt.subplot(2, 1, 1)
plt.plot(y_test, color='blue', label='Actual Value')
plt.title('Actual Value(green) & Predicted Value(blue)')
plt.ylabel('$Gold$ $Price$')

plt.subplot(2, 1, 2)
plt.plot(test_data_prediction, color='blue', label='Predicted Value')
plt.ylabel('$Gold$ $Price$')
plt.xlabel('$Number$ $of$ $values$')
plt.show()

# overlapping graph
plt.plot(y_test, color='green', label='Actual Value')
plt.plot(test_data_prediction, color='blue', label='Predicted Value')
plt.title('Actual vs Predicted Price')
plt.xlabel('Number of Values')
plt.ylabel('Gold Price')
plt.legend()
plt.show()

input_data = (2000, 50, 25, 1.2) # SPX, USO, SLV, EUR/USD

# changing the data type to numpy array
change_input = np.asarray(input_data)

# reshape the array
reshape_array = change_input.reshape(1,-1)

prediction = regressor.predict(reshape_array)
print(prediction)
