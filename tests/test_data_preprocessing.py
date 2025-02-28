import unittest
import pandas as pd
import os
import sys

# Add the scripts directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../scripts')
from data_preprocessing import preprocess_data

class TestDataPreprocessing(unittest.TestCase):
    def setUp(self):
        # Create a sample raw dataset for testing
        self.raw_data = pd.DataFrame({
            'Order Date': ['2023-01-01', '2023-02-01', None],
            'Ship Date': ['2023-01-05', '2023-02-05', '2023-03-05'],
            'Sales': [100, 200, 300],
            'Profit': [10, 20, None]
        })
        self.input_file = "tests/test_raw_data.csv"
        self.output_file = "tests/test_cleaned_data.csv"
        self.raw_data.to_csv(self.input_file, index=False)

    def test_preprocess_data(self):
        # Run the preprocessing function
        preprocess_data(self.input_file, self.output_file)

        # Load the cleaned data
        cleaned_data = pd.read_csv(self.output_file)

        # Test 1: Check if missing values are handled
        self.assertFalse(cleaned_data.isnull().values.any(), "Missing values were not handled properly.")

        # Test 2: Check if new features are created
        self.assertIn('Order Year', cleaned_data.columns, "'Order Year' column is missing.")
        self.assertIn('Order Month', cleaned_data.columns, "'Order Month' column is missing.")
        self.assertIn('Profit Margin', cleaned_data.columns, "'Profit Margin' column is missing.")

        # Test 3: Validate specific values
        self.assertEqual(cleaned_data.iloc[0]['Order Year'], 2023, "Incorrect 'Order Year' value.")
        self.assertEqual(cleaned_data.iloc[0]['Order Month'], 1, "Incorrect 'Order Month' value.")
        self.assertAlmostEqual(cleaned_data.iloc[0]['Profit Margin'], 0.1, places=2, msg="Incorrect 'Profit Margin' value.")

    def tearDown(self):
        # Clean up test files
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

if __name__ == "__main__":
    unittest.main()