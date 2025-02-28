import pandas as pd

# Path to the raw dataset
file_path = "data/raw/sales_data.csv"

# Load the dataset
df = pd.read_csv(file_path)

# Inspect the first 5 records
print("First 5 records:")
print(df.head())

# Check the shape of the dataset
print("\nDataset Shape:", df.shape)

# Check data types and missing values
print("\nData Types and Missing Values:")
print(df.info())

# Summary statistics for numerical columns
print("\nSummary Statistics:")
print(df.describe())