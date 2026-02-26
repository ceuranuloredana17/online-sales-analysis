import pandas as pd
from data_cleaning import clean_orders, clean_details
from merge_data import merge_datasets

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

if __name__ == "__main__":
    main()