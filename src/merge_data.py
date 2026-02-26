import pandas as pd

def merge_datasets(orders_df, details_df):
    """
    Merge Orders and Details datasets using Order ID as primary key.
    """

    merged_df = pd.merge(
        orders_df,
        details_df,
        on="Order ID",
        how="inner"
    )

    return merged_df