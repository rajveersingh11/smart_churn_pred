import pandas as pd
from sklearn.model_selection import train_test_split


def split_data(input_path):

    df = pd.read_csv(input_path)

    X = df.drop("churn", axis=1)
    y = df["churn"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    X_train.to_csv("data/processed/X_train.csv", index=False)
    X_test.to_csv("data/processed/X_test.csv", index=False)
    y_train.to_csv("data/processed/y_train.csv", index=False)
    y_test.to_csv("data/processed/y_test.csv", index=False)

    print("Train-test split completed")


def main():

    split_data("data/processed/ml_ready_day2.csv")


if __name__ == "__main__":
    main()
