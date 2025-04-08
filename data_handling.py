# data_handling.py

import os
import csv
from datetime import datetime

def read_csv(file_path):
    """Reads a CSV file and returns a list of rows, where each row is a dictionary."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Error: The file '{file_path}' does not exist.")

    data = []
    with open(file_path, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['transaction_date'] = datetime.strptime(row['transaction_date'],
                                                        '%Y-%m-%d')
            row['amount_spent'] = float(row['amount_spent'])
            row['user_age'] = int(row['user_age'])
            row['user_income'] = float(row['user_income'])
            data.append(row)

    return data

def get_column_data(data, column_name):
    """Extracts data for a specific column."""
    return [row[column_name] for row in data]
