from fpdf import FPDF
import pandas as pd

# Load cleaned data
df = pd.read_csv("data/processed/cleaned_sales_data.csv")

# Summary statistics
summary_stats = df.describe()

# Model performance (load the trained model and evaluate)
import joblib
model = joblib.load("models/sales_forecasting_model.pkl")
X = df[['Order Month', 'Profit Margin']]
y = df['Sales']
y_pred = model.predict(X)
mse = ((y - y_pred) ** 2).mean()

# Create a PDF report
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", size=12)

# Add content to the PDF
pdf.cell(200, 10, txt="Sales Forecasting Report", ln=True, align="C")
pdf.ln(10)

pdf.cell(200, 10, txt="1. Dataset Overview:", ln=True)
pdf.cell(200, 10, txt=f"- Total Records: {len(df)}", ln=True)
pdf.cell(200, 10, txt=f"- Average Sales: ${df['Sales'].mean():.2f}", ln=True)
pdf.cell(200, 10, txt=f"- Average Profit Margin: {df['Profit Margin'].mean() * 100:.2f}%", ln=True)
pdf.ln(10)

pdf.cell(200, 10, txt="2. Summary Statistics:", ln=True)
for col in summary_stats.columns:
    pdf.cell(200, 10, txt=f"{col}: {summary_stats[col].to_dict()}", ln=True)
pdf.ln(10)

pdf.cell(200, 10, txt="3. Key Insights:", ln=True)
pdf.cell(200, 10, txt="- Sales trends show variability over time, with noticeable peaks during certain months.", ln=True)
pdf.cell(200, 10, txt="- Profit margins vary significantly across products and regions.", ln=True)
pdf.cell(200, 10, txt=f"- The top-performing region in terms of sales is {df.groupby('Region')['Sales'].sum().idxmax()}.", ln=True)
pdf.cell(200, 10, txt=f"- The most profitable category is {df.groupby('Category')['Profit'].sum().idxmax()}.", ln=True)
pdf.ln(10)

pdf.cell(200, 10, txt="4. Model Performance:", ln=True)
pdf.cell(200, 10, txt=f"- Mean Squared Error (MSE): {mse:.2f}", ln=True)
pdf.cell(200, 10, txt="- The model predicts sales based on features like Order Month and Profit Margin.", ln=True)

# Save the PDF
pdf.output("reports/sales_forecast_report.pdf")
print("PDF report generated successfully!")