import pandas as pd

#  raw data

customers = pd.read_csv("data/raw/customers.csv")
payments = pd.read_csv("data/raw/payments.csv")
usage = pd.read_csv("data/raw/usage_metrics.csv")
support = pd.read_csv("data/raw/support_tickets.csv")

print("Files Loaded Successfully")
print("Customers:", customers.shape)
print("Payments:", payments.shape)
print("Usage:", usage.shape)
print("Support:", support.shape)
