## “E-Commerce Customer Purchase Analysis & Sales Prediction System”

# Import necessary libraries
import pandas as pd                                     # For handling dataset
import matplotlib.pyplot as plt                         # For visualization
from sklearn.model_selection import train_test_split    # For splitting data
from sklearn.linear_model import LinearRegression       # ML model
from sklearn.metrics import mean_absolute_error         # To evaluate model

# Load the dataset
df = pd.read_csv(r"D:\DS_AI_Internship\src\ecommerce_data.csv")

# Display first 5 rows
print(df.head())

# Check data types
print(df.dtypes)

# Check missing values
print(df.isna().sum())

# Bar chart: Average purchase by Gender
df.groupby("Gender")["Purchase_Amount"].mean().plot(kind="bar")
plt.title("Average Purchase Amount by Gender")
plt.ylabel("Average Purchase")
plt.show()

# Scatter plot: Income vs Purchase
plt.scatter(df["Annual_Income"], df["Purchase_Amount"])
plt.title("Income vs Purchase Amount")
plt.xlabel("Annual Income")
plt.ylabel("Purchase Amount")
plt.show()

# Line plot: Spending Score trend
plt.plot(df["Customer_ID"], df["Spending_Score"])
plt.title("Spending Score Trend")
plt.xlabel("Customer ID")
plt.ylabel("Spending Score")
plt.show()

# Selecting features (input variables)
X = df[["Age", "Annual_Income", "Spending_Score"]]

# Target variable (output)
y = df["Purchase_Amount"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate model
error = mean_absolute_error(y_test, predictions)
print("Mean Absolute Error:", error)


