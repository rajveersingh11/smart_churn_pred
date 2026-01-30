import pandas as pd


def clean_data(input_path, output_path):

    df = pd.read_csv(input_path)

    print("Before Cleaning:", df.shape)

    # Fill missing ticket days
    if "last_ticket_days" in df.columns:
        df["last_ticket_days"] = df["last_ticket_days"].fillna(999)

    # Limit inactivity (outliers)
    if "days_since_last_login" in df.columns:
        df["days_since_last_login"] = df["days_since_last_login"].clip(0, 180)

    # Remove duplicates
    df = df.drop_duplicates()

    print("After Cleaning:", df.shape)

    df.to_csv(output_path, index=False)

    print("Cleaned data saved:", output_path)


def main():

    clean_data(
        "data/processed/merged_day1.csv",
        "data/processed/cleaned_day2.csv"
    )


if __name__ == "__main__":
    main()

 


