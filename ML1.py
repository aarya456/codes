import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

df = pd.read_csv('uber.csv')
print(df.head())
print(df.info())

df.dropna(inplace=True)
df.drop(['Unnamed: 0', 'key'], axis=1, inplace=True, errors='ignore')

df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'], utc=True)

df['hour'] = df['pickup_datetime'].dt.hour
df['day'] = df['pickup_datetime'].dt.day
df['month'] = df['pickup_datetime'].dt.month
df['year'] = df['pickup_datetime'].dt.year

df.drop('pickup_datetime', axis=1, inplace=True)

Q1 = df['fare_amount'].quantile(0.25)
Q3 = df['fare_amount'].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

sns.boxplot(x=df['fare_amount'])
plt.show()

df = df[(df['fare_amount'] >= lower) &
        (df['fare_amount'] <= upper)]
        
        plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True),
            annot=True, cmap='coolwarm')
plt.show()

X = df.drop('fare_amount', axis=1)
y = df['fare_amount']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

lr = LinearRegression()
lr.fit(X_train, y_train)

lr_pred = lr.predict(X_test)

rf = RandomForestRegressor(n_estimators=100,
                           random_state=42)

rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

results = pd.DataFrame({
    'Model': ['Linear Regression', 'Random Forest'],
    'R2': [r2_score(y_test, lr_pred),
           r2_score(y_test, rf_pred)],
    'RMSE': [np.sqrt(mean_squared_error(y_test, lr_pred)),
             np.sqrt(mean_squared_error(y_test, rf_pred))]
})

print(results)