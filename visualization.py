# visualization.py

import matplotlib.pyplot as plt
from collections import defaultdict
from bayesian import beta_pdf

def plot_timeseries(data, title=""):
    """Plot a time series graph for the given data."""
    plt.figure(figsize=(10, 6))
    for label, values in data.items():
        plt.plot(values, label=label)
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Amount")
    plt.legend()
    plt.show()

def plot_histogram(data, bins=10, title="Histogram of Spending", xlabel="Amount Spent", ylabel="Frequency"):
    """Plot a histogram to show the distribution of spending amounts."""
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=bins, color='skyblue', edgecolor='black')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

def plot_boxplot(data, title="Boxplot of Spending", xlabel="Amount Spent"):
    """Plot a boxplot to show the distribution of spending amounts."""
    plt.figure(figsize=(10, 6))
    plt.boxplot(data, vert=False, patch_artist=True, boxprops=dict(facecolor='lightblue', color='blue'))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.grid(True)
    plt.show()

def plot_scatter(x_data, y_data, title="Scatter Plot of Spending vs Income", xlabel="Income", ylabel="Amount Spent"):
    """Create a scatter plot to show the relationship between two variables (income vs. spending)."""
    plt.figure(figsize=(10, 6))
    plt.scatter(x_data, y_data, color='blue', alpha=0.5)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

def plot_bar_chart(data, categories, title="Total Spending by Location", xlabel="Location", ylabel="Total Spending"):
    """Plot a bar chart to show total spending by location."""
    location_spending = defaultdict(float)
    for i, location in enumerate(categories):
        location_spending[location] += data[i]

    locations = list(location_spending.keys())
    spending = list(location_spending.values())

    plt.figure(figsize=(10, 6))
    plt.bar(locations, spending, color='teal')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

def plot_cumulative_spending(dates, spending_data, title="Cumulative Spending Over Time", xlabel="Date",
                             ylabel="Cumulative Spending"):
    """Plot a line graph for cumulative spending over time."""
    cumulative_spending = [sum(spending_data[:i + 1]) for i in range(len(spending_data))]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, cumulative_spending, color='green', marker='o', linestyle='-', linewidth=2)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()


def plot_beta_distribution(alpha, beta, title="Beta Distribution", xlabel="Probability", ylabel="Density"):
    """Plot a Beta distribution using the beta_pdf function."""
    x = [i / 1000 for i in range(1001)]  # Generate 1000 points between 0 and 1
    y = [beta_pdf(alpha, beta, val) for val in x]
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=f'Beta({alpha}, {beta})', color='blue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.legend()
    plt.show()
