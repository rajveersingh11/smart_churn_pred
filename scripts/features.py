import pandas as pd


def create_features(input_path, output_path):

    df = pd.read_csv(input_path)

    # Payment delay flag
    df["payment_delay_flag"] = (
        df["payment_delay_days"] > 15
    ).astype(int)

    # Low usage flag
    df["low_usage_flag"] = (
        df["avg_weekly_usage_hours"] < 3
    ).astype(int)

    # Support intensity
    df["support_intensity"] = (
        df["tickets_raised"] /
        (df["days_since_last_login"] + 1)
    )

    # Account age
    df["signup_date"] = pd.to_datetime(df["signup_date"])

    df["account_age_days"] = (
        pd.Timestamp.today() - df["signup_date"]
    ).dt.days

     #churn label (business rule)

    df["churn"] = (
       (df["days_since_last_login"] > 60) |
       (df["payment_delay_days"] > 30) |
       (df["failed_payments_count"] > 2)
    ).astype(int) 

    df.to_csv(output_path, index=False)

    print("Features created:", output_path)

   



def main():

    create_features(
        "data/processed/cleaned_day2.csv",
        "data/processed/featured_day2.csv"
    )


if __name__ == "__main__":
    main()
