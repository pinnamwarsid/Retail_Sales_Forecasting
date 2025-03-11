# Retail Sales Forecasting Dashboard

![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)

This project focuses on building a Retail Sales Forecasting System that predicts future sales based on historical data. The system includes:

1. Data preprocessing and cleaning.
2. A machine learning model for sales forecasting.
3. A Power BI dashboard for visualizing insights and trends.
4. Comprehensive reporting and evaluation metrics.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Power BI Dashboard](#power-bi-dashboard)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Overview
The goal of this project is to analyze retail sales data, predict future sales using machine learning, and provide actionable insights through visualizations and reports. The system is designed to help businesses make data-driven decisions by understanding sales trends, profit margins, and regional performance.

Key components include:
- Data Preprocessing: Cleaning and transforming raw sales data.
- Forecasting Model: Predicting sales using a trained machine learning model.
- Power BI Dashboard: Interactive visualizations for sales trends, profit margins, and regional performance.
- Reporting: Generating detailed reports summarizing insights and model performance.

## Features

### Data Pipeline:
- Load, clean, and preprocess raw sales data.
- Handle missing values and create new features (e.g., Order Year, Profit Margin).

### Machine Learning:
- Train a forecasting model to predict sales based on features like Order Month and Profit Margin.
- Evaluate model performance using metrics like Mean Squared Error (MSE) and R-squared.

### Reporting:
- Generate PDF reports summarizing insights, model performance, and key statistics from the dataset.
- Key insights include sales trends, profit margins, and top-performing regions and categories.

### Power BI Dashboard:
- Visualize sales trends, profit margins, and regional performance.
- Compare actual vs. predicted sales.

## Installation

### Prerequisites
- Python 3.7 or higher
- Power BI Desktop (for the dashboard)

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/pinnamwarsid/repo.git
   ```
2. Navigate to the project directory:
   ```bash
   cd repo
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the project, execute the following command:
```bash
python scripts/data_preprocessing.py
```
This will preprocess the data and prepare it for forecasting.

To generate a sales forecasting report, run:
```bash
python scripts/generate_report.py
```

## Project Structure
```
Retail_Sales_Forecasting/
│
├── data/                     # Contains raw and processed data
│   ├── raw/                  # Raw sales data
│   └── processed/            # Cleaned sales data
│
├── logs/                     # Log files for model training and preprocessing
│
├── models/                   # Trained machine learning models
│
├── notebooks/                # Jupyter notebooks for data analysis and modeling
│
├── powerbi_dashboard/        # Power BI dashboard files
│
├── reports/                  # Generated reports and visualizations
│
├── scripts/                  # Python scripts for data processing and forecasting
│
├── tests/                    # Unit tests for the project
│
├── requirements.txt          # Python package dependencies
└── README.md                 # Project documentation

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a description of your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or support, please reach out to:
- Pinnamwar Sai Siddanth - pinnamwarsid@gmail.com
