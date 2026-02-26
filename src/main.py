import pandas as pd
from data_cleaning import clean_orders, clean_details
from merge_data import merge_datasets

from kpi_analysis import (
    calculate_kpis,
    revenue_by_state,
    monthly_revenue,
    profit_by_category,
    top_customers
)

from visualization import (
    plot_monthly_revenue,
    plot_revenue_by_state,
    plot_profit_by_category,
    plot_top_customers
)


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

    print("\nCalculating KPIs...")
    kpis = calculate_kpis(merged_df)

    for key, value in kpis.items():
        print(f"{key}: {value:.2f}")

    print("\nMonthly Revenue:")
    monthly_rev = monthly_revenue(merged_df)
    print(monthly_rev)
    plot_monthly_revenue(monthly_rev)

    print("\nRevenue by State:")
    state_rev = revenue_by_state(merged_df)
    print(state_rev.head())
    plot_revenue_by_state(state_rev)

    print("\nProfit by Category:")
    category_profit = profit_by_category(merged_df)
    print(category_profit)
    plot_profit_by_category(category_profit)

    print("\nTop 10 Customers:")
    top_cust = top_customers(merged_df)
    print(top_cust)
    plot_top_customers(top_cust)


if __name__ == "__main__":
    main()