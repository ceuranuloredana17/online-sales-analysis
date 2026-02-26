import pandas as pd

def clean_orders(df):
    df = df.copy()
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    df = df.drop_duplicates()
    df = df.dropna()
    return df


def clean_details(df):
    df = df.copy()
    df = df.drop_duplicates()
    df = df.dropna()
    return df