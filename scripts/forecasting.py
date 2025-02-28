import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib
import logging

# Configure logging
logging.basicConfig(filename="logs/model_training.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def train_forecasting_model(input_file, model_file):
    try:
        # Load cleaned data
        df = pd.read_csv(input_file)
        logging.info("Cleaned data loaded successfully.")

        # Feature selection
        X = df[['Order Month', 'Profit Margin']]  # Example features
        y = df['Sales']

        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        logging.info("Data split into training and testing sets.")

        # Train model
        model = LinearRegression()
        model.fit(X_train, y_train)
        logging.info("Model training completed.")

        # Evaluate model
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        logging.info(f"Model MSE: {mse}")

        # Save model
        joblib.dump(model, model_file)
        logging.info(f"Model saved to {model_file}.")

    except Exception as e:
        logging.error(f"Error during model training: {e}")

if __name__ == "__main__":
    train_forecasting_model("data/processed/cleaned_sales_data.csv", "models/sales_forecasting_model.pkl")