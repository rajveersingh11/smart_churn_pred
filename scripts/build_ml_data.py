import pandas as pd


def build_ml_data(input_path, output_path):

    df = pd.read_csv(input_path)

    features = [
        "payment_delay_flag",
        "low_usage_flag",
        "support_intensity",
        "account_age_days",
        "days_since_last_login",
        "failed_payments_count"
    ]

    target = ["churn"]

    final_df = df[features + target]

    final_df.to_csv(output_path, index=False)

    print("ML-ready dataset saved:", output_path)


def main():

    build_ml_data(
        "data/processed/featured_day2.csv",
        "data/processed/ml_ready_day2.csv"
    )


if __name__ == "__main__":
    main()
