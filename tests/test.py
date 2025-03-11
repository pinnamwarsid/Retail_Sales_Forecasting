"""import pandas as pd

df_forecast = pd.read_csv("results/forecasted_sales.csv")
print(f"Total Forecasted Sales: ${df_forecast['Predicted Sales'].sum():,.2f}") """

import requests

url = "http://127.0.0.1:8000/chat"
data = {"message": "What is next month's sales forecast?"}
response = requests.post(url, json=data)

print(response.json())  # Expected: {"response": "Predicted total sales for next month: $2,254,832.52"}
