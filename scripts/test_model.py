import joblib
import pandas as pd

# Path to the saved model
model_file = "models/sales_forecasting_model.pkl"

# Load the model
try:
    model = joblib.load(model_file)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading the model: {e}")
    exit()

# Load the cleaned dataset for testing
data_file = "data/processed/cleaned_sales_data.csv"
df = pd.read_csv(data_file)

# Prepare test data
X_test = df[['Order Month', 'Profit Margin']].head(5)  # Use the first 5 rows for testing
print("\nTest Data (First 5 Rows):")
print(X_test)

# Make predictions
try:
    predictions = model.predict(X_test)
    print("\nPredictions:")
    print(predictions)
except Exception as e:
    print(f"Error making predictions: {e}")