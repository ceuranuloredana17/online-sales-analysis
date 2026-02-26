def calculate_kpis(df):
    total_revenue = df["Amount"].sum()
    total_profit = df["Profit"].sum()
    profit_margin = (total_profit / total_revenue) * 100

    return {
        "Total Revenue": total_revenue,
        "Total Profit": total_profit,
        "Profit Margin (%)": profit_margin
    }


def revenue_by_state(df):
    return df.groupby("State")["Amount"].sum().sort_values(ascending=False)


def monthly_revenue(df):
    df = df.copy()
    df["Month"] = df["Order Date"].dt.to_period("M")
    return df.groupby("Month")["Amount"].sum().sort_index()


def profit_by_category(df):
    return df.groupby("Category")["Profit"].sum().sort_values(ascending=False)


def top_customers(df, n=10):
    return (
        df.groupby("CustomerName")["Amount"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
    )