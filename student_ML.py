import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Sample data
data = {
    'Study Hours': [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0],
    'Marks': [35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Visualize the data
plt.scatter(df['Study Hours'], df['Marks'], color='blue')
plt.title('Study Hours vs Marks')
plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.show()

# Prepare the data
X = df[['Study Hours']]  # Independent variable
y = df['Marks']          # Dependent variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict marks for the test set
y_pred = model.predict(X_test)

# Compare actual and predicted marks
comparison = pd.DataFrame({'Actual Marks': y_test, 'Predicted Marks': y_pred})
print(comparison)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Visualize the regression line
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')  # Regression line
plt.title('Study Hours vs Marks (with Regression Line)')
plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.show()
