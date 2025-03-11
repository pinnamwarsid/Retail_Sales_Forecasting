from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import logging
import os

# Configure logging
logging.basicConfig(filename="logs/chatbot.log", level=logging.INFO, format="%(asctime)s - %(message)s")

app = FastAPI()

# Load data files
data_files = {
    "Cleaned Data": "data/processed/cleaned_sales_data.csv",
    "Forecasted Data": "results/forecasted_sales.csv",
    "Evaluation Metrics": "results/model_evaluation.csv",
    "README": "README.md",
    "Requirements": "requirements.txt"
}

loaded_data = {}

try:
    for name, path in data_files.items():
        if os.path.exists(path):
            if path.endswith(".csv"):
                df = pd.read_csv(path)
                loaded_data[name] = {
                    "df": df,
                    "columns": list(df.columns),
                    "row_count": len(df),
                    "preview": df.head(3).to_dict()
                }
            else:
                with open(path, "r", encoding="utf-8") as file:
                    loaded_data[name] = file.read()
        else:
            loaded_data[name] = f"{name} not found."
    logging.info("Data files loaded successfully.")
except Exception as e:
    logging.error(f"Error loading data files: {e}")

# Define request model
class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat_with_bot(request: ChatRequest):
    user_input = request.message.lower()
    logging.info(f"Received query: {user_input}")

    # Total Sales
    if "total sales" in user_input and "next month" not in user_input:
        total_sales = loaded_data["Cleaned Data"]["df"]["Sales"].sum()
        return {"response": f"Total sales so far: ${total_sales:,.2f}"}

    # Forecasted Sales
    elif "next month's sales" in user_input or "sales forecast" in user_input or "predicted sales" in user_input:
        logging.info("Forecast query received")
        if "Predicted Sales" in loaded_data["Forecasted Data"]["columns"]:
            next_month_sales = loaded_data["Forecasted Data"]["df"]["Predicted Sales"].sum()
            logging.info(f"Calculated predicted sales for next month: ${next_month_sales:,.2f}")
            return {"response": f"Predicted total sales for next month: ${next_month_sales:,.2f}"}
        else:
            return {"response": "Forecast data is unavailable."}

    # Average Sales per Transaction
    elif "average sales" in user_input and "product" not in user_input:
        avg_sales = loaded_data["Cleaned Data"]["df"]["Sales"].mean()
        return {"response": f"Average sales per transaction: ${avg_sales:,.2f}"}

    # Average Sales per Product
    elif "average sales per product" in user_input or "mean sales per product" in user_input:
        if "Product Name" in loaded_data["Cleaned Data"]["columns"]:
            product_sales = loaded_data["Cleaned Data"]["df"].groupby("Product Name")["Sales"].sum()
            avg_sales_per_product = product_sales.mean()
            logging.info(f"Calculated average sales per product: ${avg_sales_per_product:,.2f}")
            return {"response": f"Average sales per product: ${avg_sales_per_product:,.2f}"}
        else:
            return {"response": "Product sales data is currently unavailable in the dataset."}

    # Best-Selling Product
    elif "best selling product" in user_input or "top product" in user_input:
        if "Product Name" in loaded_data["Cleaned Data"]["columns"]:
            product_sales = loaded_data["Cleaned Data"]["df"].groupby("Product Name")["Sales"].sum()
            top_product = product_sales.idxmax()
            return {"response": f"Best-selling product: {top_product}"}
        else:
            return {"response": "Product sales data is currently unavailable in the dataset."}

    # Lowest-Selling Product
    elif "lowest selling product" in user_input or "least selling product" in user_input:
        if "Product Name" in loaded_data["Cleaned Data"]["columns"]:
            product_sales = loaded_data["Cleaned Data"]["df"].groupby("Product Name")["Sales"].sum()
            bottom_product = product_sales.idxmin()
            return {"response": f"Lowest-selling product: {bottom_product}"}
        else:
            return {"response": "Product sales data is currently unavailable in the dataset."}

    # Best-Selling Region
    elif "highest selling region" in user_input or "top region" in user_input:
        if "Region" in loaded_data["Cleaned Data"]["columns"]:
            region_sales = loaded_data["Cleaned Data"]["df"].groupby("Region")["Sales"].sum()
            best_region = region_sales.idxmax()
            return {"response": f"Highest selling region: {best_region}"}
        else:
            return {"response": "Region sales data is currently unavailable in the dataset."}

    # Lowest-Selling Region
    elif "lowest selling region" in user_input or "worst region" in user_input:
        if "Region" in loaded_data["Cleaned Data"]["columns"]:
            region_sales = loaded_data["Cleaned Data"]["df"].groupby("Region")["Sales"].sum()
            worst_region = region_sales.idxmin()
            return {"response": f"Lowest selling region: {worst_region}"}
        else:
            return {"response": "Region sales data is currently unavailable in the dataset."}

    # Model Performance
    elif "model accuracy" in user_input or "how accurate is the model" in user_input or "model performance" in user_input:
        logging.info("Model evaluation query received")
        try:
            mse = loaded_data["Evaluation Metrics"]["df"].loc[loaded_data["Evaluation Metrics"]["df"]['Metric'] == 'Mean Squared Error', 'Value'].values[0]
            r2 = loaded_data["Evaluation Metrics"]["df"].loc[loaded_data["Evaluation Metrics"]["df"]['Metric'] == 'R-squared', 'Value'].values[0]
            logging.info(f"Model Performance - MSE: {mse:.2f}, R² Score: {r2:.2f}")
            return {"response": f"Model Performance:\n- MSE: {mse:.2f}\n- R² Score: {r2:.2f}"}
        except Exception as e:
            return {"response": "Unable to retrieve model performance details. Please check the evaluation metrics."}

    # Project Details
    elif "what is this project about" in user_input or "explain about project" in user_input or "about project" in user_input:
        return {"response": "This is a Sales Forecasting project that processes sales data, builds predictive models, evaluates model performance, and generates reports."}

    elif "what are the requirements" in user_input or "requirements" in user_input or "what's required" in user_input or "project requirements" in user_input:
        with open("requirements.txt", "r") as req_file:
            requirements = req_file.read()
        return {"response": f"The project requirements are:\n{requirements}"}

    elif "what reports are available" in user_input or "available reports" in user_input or "reports" in user_input or "project reports" in user_input:
        reports = ", ".join(data_files.keys())
        return {"response": f"The available reports are: {reports}."}

    elif "how much data is there" in user_input or "data statistics" in user_input or "data info" in user_input or "data details" in user_input or "data amount" in user_input:
        total_rows = loaded_data["Cleaned Data"]["row_count"]
        mean_sales = loaded_data["Cleaned Data"]["df"]["Sales"].mean()
        median_sales = loaded_data["Cleaned Data"]["df"]["Sales"].median()
        return {
            "response": f"There are {total_rows} rows of data. Mean sales: ${mean_sales:,.2f}, Median sales: ${median_sales:,.2f}."
        }

    else:
        return {"response": "I'm here to assist you with sales data, forecasts, and insights. Please ask specific questions!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)