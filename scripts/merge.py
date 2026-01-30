import pandas as pd

customers = pd.read_csv("data/raw/customers.csv")
payments = pd.read_csv("data/raw/payments.csv")
usage = pd.read_csv("data/raw/usage_metrics.csv")
support = pd.read_csv("data/raw/support_tickets.csv")

# Merge all on customer_id
df = customers.merge(payments, on="customer_id") \
              .merge(usage, on="customer_id") \
              .merge(support, on="customer_id")

df.to_csv("data/processed/merged_day1.csv", index=False)

print("Merged dataset saved")
print("Shape:", df.shape)
