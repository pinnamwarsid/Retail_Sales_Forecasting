import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error, r2_score

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
y_pred = model.predict(X_test)

# Calculate evaluation metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Save evaluation metrics to a CSV file
output_file = "results/model_evaluation.csv"
pd.DataFrame({
    'Metric': ['Mean Squared Error', 'R-squared'],
    'Value': [mse, r2]
}).to_csv(output_file, index=False)

print(f"Evaluation metrics saved to {output_file}")