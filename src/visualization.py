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