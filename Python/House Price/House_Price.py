import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')

# Dataset: Ames Housing Dataset (Kaggle: https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data)
housing_data = pd.read_csv("/train.csv")  # Replace with your path

print("Dataset Overview:")
print(housing_data.head())
print(f"\nDataset shape: {housing_data.shape}")
print("\nDataset info:")
print(housing_data.info())

# Data preprocessing for housing data
print("\n" + "="*50)
print("DATA PREPROCESSING FOR HOUSING VALUATION")
print("="*50)

# Select key features relevant for house valuation (similar to gold's financial features)
key_features = [
    'LotArea', 'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd',
    '1stFlrSF', '2ndFlrSF', 'GrLivArea', 'FullBath', 'TotRmsAbvGrd',
    'GarageArea', 'GarageCars', 'MSSubClass', 'LotFrontage'
]

# Handle missing values
housing_data[key_features] = housing_data[key_features].fillna(housing_data[key_features].median())

# Target variable
target = 'SalePrice'

# Features and target
X = housing_data[key_features]
y = housing_data[target]

print(f"\nSelected Features ({len(key_features)}): {key_features}")
print(f"Target: {target}")
print(f"\nFeature statistics:")
print(X.describe())

# Correlation heatmap (similar to gold correlation analysis)
plt.figure(figsize=(12,10))
correlation = X.corr()
sns.heatmap(correlation, cbar=True, square=True, annot=True, annot_kws={'size': 8}, cmap='Blues')
plt.title('Feature Correlation Matrix for House Valuation')
plt.tight_layout()
plt.show()

# Distribution of house prices (similar to gold price distribution)
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
sns.histplot(y, kde=True, color='orange')
plt.title('Distribution of House Sale Prices')

plt.subplot(1,2,2)
sns.boxplot(y=y, color='orange')
plt.title('Boxplot of House Sale Prices')
plt.tight_layout()
plt.show()

# Train-test split (same methodology as gold)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=1)
print(f"\nTraining set: {X_train.shape}, Test set: {X_test.shape}")

# Same RandomForest model architecture
regressor = RandomForestRegressor(n_estimators=100, random_state=1)
regressor.fit(X_train, y_train)
print("✅ Model trained successfully!")

# Predictions
test_predictions = regressor.predict(X_test)
print(f"\nSample predictions: {test_predictions[:5]}")
print(f"Actual test values: {y_test.iloc[:5].values}")

# Model performance metrics (same as gold)
r2_score = metrics.r2_score(y_test, test_predictions)
print(f"\n📊 Model Performance:")
print(f"R² Score: {r2_score:.4f}")
print(f"MAE: ${metrics.mean_absolute_error(y_test, test_predictions):,.0f}")
print(f"RMSE: ${np.sqrt(metrics.mean_squared_error(y_test, test_predictions)):.0f}")

# Visualization (same style as gold prediction)
plt.figure(figsize=(15,10))

# Subplot 1: Actual vs Predicted
plt.subplot(2,2,1)
plt.plot(y_test.values, color='green', label='Actual Price', alpha=0.7)
plt.plot(test_predictions, color='blue', label='Predicted Price', alpha=0.7)
plt.title('Actual vs Predicted House Prices')
plt.xlabel('Number of Test Samples')
plt.ylabel('Sale Price ($)')
plt.legend()

# Subplot 2: Scatter plot
plt.subplot(2,2,2)
plt.scatter(y_test, test_predictions, alpha=0.6, color='purple')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Actual Price ($)')
plt.ylabel('Predicted Price ($)')
plt.title(f'Actual vs Predicted (R² = {r2_score:.3f})')

# Subplot 3: Feature importance (NEW - specific to housing)
plt.subplot(2,2,3)
importances = regressor.feature_importances_
feature_importance = pd.DataFrame({
    'feature': key_features,
    'importance': importances
}).sort_values('importance', ascending=True)

plt.barh(feature_importance['feature'], feature_importance['importance'])
plt.title('Feature Importance for House Valuation')
plt.xlabel('Importance Score')

# Subplot 4: Residuals
plt.subplot(2,2,4)
residuals = y_test.values - test_predictions
plt.scatter(test_predictions, residuals, alpha=0.6, color='red')
plt.axhline(y=0, color='black', linestyle='--')
plt.xlabel('Predicted Price ($)')
plt.ylabel('Residuals ($)')
plt.title('Residuals Plot')

plt.tight_layout()
plt.show()

# 🔥 REAL-WORLD INVESTMENT EXAMPLE
print("\n" + "="*60)
print("🏠 REAL ESTATE INVESTMENT VALUATION EXAMPLE")
print("="*60)

# New property for investment analysis (similar to gold's input_data)
investment_property = {
    'LotArea': 8500,        # Square feet
    'OverallQual': 7,       # Quality rating (1-10)
    'OverallCond': 6,       # Condition rating (1-10)
    'YearBuilt': 2005,      # Year built
    'YearRemodAdd': 2005,   # Year remodeled
    '1stFlrSF': 1800,       # First floor sq ft
    '2ndFlrSF': 800,        # Second floor sq ft
    'GrLivArea': 2600,      # Above ground living area
    'FullBath': 2,          # Full bathrooms
    'TotRmsAbvGrd': 8,      # Total rooms above ground
    'GarageArea': 500,      # Garage area sq ft
    'GarageCars': 2,        # Garage capacity
    'MSSubClass': 60,       # Type of dwelling
    'LotFrontage': 75       # Lot frontage ft
}

# Convert to numpy array (same as gold)
input_array = np.array(list(investment_property.values())).reshape(1, -1)

# Get instant valuation
predicted_price = regressor.predict(input_array)[0]
print(f"\n📈 INVESTMENT PROPERTY VALUATION:")
print(f"Property Features: {investment_property}")
print(f"🎯 ESTIMATED MARKET VALUE: ${predicted_price:,.0f}")
print(f"💰 Investment Score: {'EXCELLENT' if predicted_price > 250000 else 'GOOD' if predicted_price > 200000 else 'FAIR'}")

# Multiple investment scenarios
scenarios = [
    "FIXER-UPPER (Low Quality)", 
    "AVERAGE HOME", 
    "PREMIUM PROPERTY"
]

scenario_data = [
    [7500, 5, 4, 1990, 1990, 1200, 0, 1200, 1, 6, 300, 1, 60, 60],  # Fixer-upper
    [8000, 6, 5, 2000, 2000, 1600, 600, 2200, 2, 7, 400, 2, 60, 70],  # Average
    [10000, 8, 7, 2015, 2015, 2200, 1200, 3400, 3, 10, 700, 3, 60, 90] # Premium
]

print(f"\n🏆 BATCH VALUATION - {len(scenarios)} Investment Opportunities:")
for i, scenario in enumerate(scenarios):
    pred = regressor.predict([scenario_data[i]])[0]
    status = "🟢 BUY" if pred > 250000 else "🟡 HOLD" if pred > 200000 else "🔴 PASS"
    print(f"{scenario:20} | ${pred:>9,.0f} | {status}")

print("\n✅ Model ready for real-time property investment analysis!")
