import pandas as pd
import joblib

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


def train_models():

    X_train = pd.read_csv("data/processed/X_train.csv")
    y_train = pd.read_csv("data/processed/y_train.csv").values.ravel()

    models = {
        "logistic": LogisticRegression(max_iter=1000),
        "decision_tree": DecisionTreeClassifier(max_depth=6),
        "random_forest": RandomForestClassifier(
            n_estimators=200,
            random_state=42
        )
    }

    for name, model in models.items():

        model.fit(X_train, y_train)

        joblib.dump(
            model,
            f"data/models/{name}.pkl"
        )

        print(f"{name} model trained")


def main():

    train_models()


if __name__ == "__main__":
    main()
