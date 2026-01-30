import pandas as pd


def validate_data(path):

    df = pd.read_csv(path)

    print("Dataset Shape:", df.shape)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nStatistics:")
    print(df.describe())

    print("\nCorrelation with Churn:")
    print(df.corr(numeric_only=True)["churn"])


def main():

    validate_data("data/processed/featured_day2.csv")


if __name__ == "__main__":
    main()
