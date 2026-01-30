import pandas as pd

customers = pd.read_csv("data/raw/customers.csv")

print("Missing Values:")
print(customers.isnull().sum())

print("\nStatistics:")
print(customers.describe())

print("\nDuplicates:")
print(customers.duplicated().sum())

payments = pd.read_csv("data/raw/payments.csv")

print("\nPayments Missing Values:")
print(payments.isnull().sum())

print("\nPayments Statistics:")
print(payments.describe())



