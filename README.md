# 📊 Online Sales Data Analysis

## 📌 Project Overview

This project performs an end-to-end business analysis on an online retail dataset using Python.

The dataset consists of two relational tables:

- **Orders.csv** – Customer and order information
- **Details.csv** – Product-level details for each order

The goal of this project is to simulate a real-world business intelligence workflow, including:

- Data cleaning
- Relational dataset merging
- KPI calculation
- Time-series analysis
- Dimensional breakdown analysis
- Data visualization

---

## 🛠 Technologies Used

- Python
- Pandas
- Matplotlib
- Virtual Environment (venv)

---

## 🗂 Project Structure
online-sales-analysis/
│
├── data/
│ ├── Orders.csv
│ ├── Details.csv
│
├── src/
│ ├── main.py
│ ├── data_cleaning.py
│ ├── merge_data.py
│ ├── kpi_analysis.py
│ └── visualization.py
│
├── outputs/
├── venv/


---

## 🔄 Data Processing Pipeline

1. Load datasets
2. Clean missing values and duplicates
3. Merge datasets using `Order ID` as primary key
4. Calculate business KPIs
5. Generate analytical insights
6. Visualize results

---

## 📈 Key Business KPIs

- **Total Revenue:** 192,011
- **Total Profit:** 17,368
- **Profit Margin:** 9.05%

---

## 📊 Analysis Performed

### 📅 Monthly Revenue Trend
Time-series analysis showing seasonal revenue fluctuations.

### 📍 Revenue by State
Top-performing states based on total sales.

### 🏆 Profit by Category
Comparison of profitability across product categories.

### 👥 Top 10 Customers
Customers generating the highest revenue.

---

## 🧠 Business Insights

- October generated the highest revenue.
- Profit margin is approximately 9%, indicating moderate profitability.
- Revenue distribution varies significantly across states.
- Certain product categories outperform others in profitability.

