import pandas as pd
import logging

# Configure logging
logging.basicConfig(filename="logs/preprocessing.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def preprocess_data(input_file, output_file):
    try:
        # Load raw data
        df = pd.read_csv(input_file)
        logging.info("Raw data loaded successfully.")

        # Convert date columns to datetime
        df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
        df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')
        logging.info("Converted 'Order Date' and 'Ship Date' to datetime.")

        # Handle missing values
        if df.isnull().sum().sum() > 0:
            df.fillna(method='ffill', inplace=True)  # Forward fill missing values
            logging.info("Handled missing values using forward fill.")

        # Create new features
        df['Order Year'] = df['Order Date'].dt.year
        df['Order Month'] = df['Order Date'].dt.month
        df['Profit Margin'] = df['Profit'] / df['Sales']
        logging.info("Created new features: Order Year, Order Month, and Profit Margin.")

        # Save cleaned data
        df.to_csv(output_file, index=False)
        logging.info(f"Cleaned data saved to {output_file}.")

    except Exception as e:
        logging.error(f"Error during preprocessing: {e}")

if __name__ == "__main__":
    preprocess_data("data/raw/sales_data.csv", "data/processed/cleaned_sales_data.csv")