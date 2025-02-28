import unittest
import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error
import sys
import os

# Add the scripts directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../scripts')
from forecasting import train_forecasting_model

class TestForecasting(unittest.TestCase):
    def setUp(self):
        # Create a sample cleaned dataset for testing
        self.cleaned_data = pd.DataFrame({
            'Order Month': [1, 2, 3, 4, 5],
            'Profit Margin': [0.1, 0.2, 0.3, 0.4, 0.5],
            'Sales': [100, 200, 300, 400, 500]
        })
        self.input_file = "tests/test_cleaned_data.csv"
        self.model_file = "tests/test_model.pkl"
        self.cleaned_data.to_csv(self.input_file, index=False)

    def test_train_forecasting_model(self):
        # Train the model
        train_forecasting_model(self.input_file, self.model_file)

        # Load the trained model
        model = joblib.load(self.model_file)

        # Make predictions on the test data
        X_test = self.cleaned_data[['Order Month', 'Profit Margin']]
        y_test = self.cleaned_data['Sales']
        y_pred = model.predict(X_test)

        # Test 1: Check if predictions are generated
        self.assertEqual(len(y_pred), len(y_test), "Number of predictions does not match the test data.")

        # Test 2: Validate Mean Squared Error (MSE)
        mse = mean_squared_error(y_test, y_pred)
        self.assertLess(mse, 1000, "Mean Squared Error is too high.")

    def tearDown(self):
        # Clean up test files
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        if os.path.exists(self.model_file):
            os.remove(self.model_file)

if __name__ == "__main__":
    unittest.main()