import pandas as pd
from data_cleaning import clean_orders, clean_details
from merge_data import merge_datasets
from kpi_analysis import calculate_kpis
from kpi_analysis import calculate_kpis, revenue_by_state, monthly_revenue
from visualization import plot_monthly_revenue


def main():
    print("Loading datasets...")

    orders = pd.read_csv("data/Orders.csv")
    details = pd.read_csv("data/Details.csv")

    print("Cleaning data...")
    orders = clean_orders(orders)
    details = clean_details(details)

    print("Merging datasets...")
    merged_df = merge_datasets(orders, details)

    print("Preview merged data:")
    print(merged_df.head())

    print("Calculating KPIs...")
    kpis = calculate_kpis(merged_df)

    print("\nMonthly Revenue:")
    monthly_rev = monthly_revenue(merged_df)
    print(monthly_rev)

    for key, value in kpis.items():
        print(f"{key}: {value:.2f}")


if __name__ == "__main__":
    main()