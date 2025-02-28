import pandas as pd
import joblib

# Load the cleaned dataset
data_file = "data/processed/cleaned_sales_data.csv"
df = pd.read_csv(data_file)

# Load the trained model
model_file = "models/sales_forecasting_model.pkl"
model = joblib.load(model_file)

# Prepare test data
X_test = df[['Order Month', 'Profit Margin']]
y_test = df['Sales']

# Make predictions
predictions = model.predict(X_test)

# Save predictions to a CSV file
output_file = "results/forecasted_sales.csv"
pd.DataFrame({
    'Order Month': X_test['Order Month'],
    'Profit Margin': X_test['Profit Margin'],
    'Actual Sales': y_test,
    'Predicted Sales': predictions
}).to_csv(output_file, index=False)

print(f"Predictions saved to {output_file}")