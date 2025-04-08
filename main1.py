# main.py

from data_handling import *
from my_statistics import *
from outliers import *
from visualization import *
from bayesian import *

def main():
    data = read_csv('user_transactions.csv')

    amount_spent_data = get_column_data(data, 'amount_spent')
    transaction_dates = get_column_data(data, 'transaction_date')
    user_age_data = get_column_data(data, 'user_age')
    user_income_data = get_column_data(data, 'user_income')
    locations = get_column_data(data, 'location')

    print("Analyzing spending trends over time...")  #Analysis of spending over time
    monthly_spending = {}
    for i, date in enumerate(transaction_dates):
        month = date.month
        if month not in monthly_spending:
            monthly_spending[month] = []
        monthly_spending[month].append(amount_spent_data[i])

    for month, spending in monthly_spending.items():
        print(f"Month {month}: Mean spending = {mean(spending)}, Median = {median(spending)}, Std Dev = {standard_deviation(spending)}")


    plot_timeseries(monthly_spending, title="Monthly Spending Trends")
    plot_cumulative_spending(transaction_dates, amount_spent_data, title="Cumulative Spending Over Time")
    plot_histogram(amount_spent_data, bins=20, title="Distribution of Spending Amounts")
    plot_boxplot(amount_spent_data, title="Boxplot of Spending Amounts")
    plot_bar_chart(amount_spent_data, locations, title="Total Spending by Location")
    plot_scatter(user_income_data, amount_spent_data, title="Spending vs. Income")

    print("\n--- Detecting anomalies using Z-score method ---")   #Anamoly detection
    anomalies_zscore = z_score_outliers(amount_spent_data, threshold=3)
    if len(anomalies_zscore) == 0:
        print("There is no anomaly present in the data.")
    else:
        print(f"Anomalies (outliers) detected using Z-score: {anomalies_zscore}")

    print("\n--- Performing correlation analysis ---")     # Correlation analysis
    age_income_corr = pearson_correlation(user_age_data, user_income_data)
    age_spending_corr = pearson_correlation(user_age_data, amount_spent_data)
    income_spending_corr = pearson_correlation(user_income_data, amount_spent_data)

    print(f"Correlation between Age and Income: {age_income_corr}")
    print(f"Correlation between Age and Spending: {age_spending_corr}")
    print(f"Correlation between Income and Spending: {income_spending_corr}")



    print("\n--- Bayesian Update (Spending Data) ---")
    prior_alpha= int(input("Enter prior alpha : "))  # Prior belief parameters
    prior_beta=int(input("Enter prior beta : "))  # Prior belief parameters
    success_spent=int(input("Enter success spending amount : "))
    successes = sum(1 for x in amount_spent_data if x > success_spent)
    failures = len(amount_spent_data) - successes
    updated_alpha, updated_beta = bayesian_update(prior_alpha, prior_beta, successes, failures)
    print(f"Updated Beta Parameters: alpha = {updated_alpha}, beta = {updated_beta}")
    plot_beta_distribution(updated_alpha, updated_beta, title="Posterior Beta Distribution")

    print("\n--- Credible Interval (Spending Data) ---")
    lower, upper = credible_interval(updated_alpha, updated_beta, confidence_level=0.95)
    print(f"Credible Interval (95%): [{lower:.3f}, {upper:.3f}]")

    print("\n--- Posterior Predictive Distribution ---")
    predictive = posterior_predictive(prior_alpha, prior_beta, [1 if x > 500 else 0 for x in amount_spent_data])
    print(f"Posterior Predictive Probabilities: {predictive}")

    print("\n--- Bayesian Inference (Income Data) ---")
    # Assume prior mean and std dev for income
    mu_prior = 4000
    sigma_prior = 1000
    observed_sigma = 500
    posterior_mean, posterior_std = bayesian_inference(user_income_data, mu_prior, sigma_prior, observed_sigma)
    print(f"Posterior Mean Income: {posterior_mean}, Posterior Std Dev: {posterior_std}")

    print("\n--- Bayesian Credible Region (Income Data) ---")
    lower_bound, upper_bound = bayesian_credible_region(user_income_data, mu_prior, sigma_prior, observed_sigma)
    print(f"Credible Region for Income (95%): [{lower_bound:.2f}, {upper_bound:.2f}]")

    print("\n--- Bayesian Hypothesis Testing ---")
    prior_odds = 1  # Equal odds for H1 and H0 initially
    likelihood_ratio = sum(user_income_data) / sum(amount_spent_data)
    posterior_odds = bayesian_hypothesis_testing(prior_odds, likelihood_ratio)
    print(f"Posterior Odds for Hypothesis (Income explains Spending): {posterior_odds:.2f}")



    print("\n--- Segmenting users based on spending behavior ---")
    high_spenders = []
    low_spenders = []
    for i, amount in enumerate(amount_spent_data):
        if amount > 1000:
            high_spenders.append(data[i]['user_id'])
        elif amount <= 100:
            if data[i]['user_id'] not in low_spenders:
                low_spenders.append(data[i]['user_id'])
    print(f"High Spenders: {high_spenders}")
    print(f"Low Spenders: {low_spenders}")


if __name__ == "__main__":
    main()
