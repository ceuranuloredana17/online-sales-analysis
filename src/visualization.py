import matplotlib.pyplot as plt
import matplotlib.pyplot as plt


def plot_monthly_revenue(monthly_data):
    plt.figure()
    monthly_data.plot()

    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()

def plot_revenue_by_state(state_data):
    plt.figure()
    state_data.head(10).plot(kind="bar")

    plt.title("Top 10 States by Revenue")
    plt.xlabel("State")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


def plot_profit_by_category(category_data):
    plt.figure()
    category_data.plot(kind="bar")

    plt.title("Profit by Category")
    plt.xlabel("Category")
    plt.ylabel("Profit")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


def plot_top_customers(customers_data):
    plt.figure()
    customers_data.plot(kind="bar")

    plt.title("Top 10 Customers by Revenue")
    plt.xlabel("Customer")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()