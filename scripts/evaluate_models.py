import pandas as pd
import joblib

from sklearn.metrics import (
    accuracy_score,
    recall_score,
    roc_auc_score
)


def evaluate_models():

    X_test = pd.read_csv("data/processed/X_test.csv")
    y_test = pd.read_csv("data/processed/y_test.csv").values.ravel()

    model_names = [
        "logistic",
        "decision_tree",
        "random_forest"
    ]

    results = {}

    for name in model_names:

        model = joblib.load(
            f"data/models/{name}.pkl"
        )

        y_pred = model.predict(X_test)
        y_prob = model.predict_proba(X_test)[:, 1]

        acc = accuracy_score(y_test, y_pred)
        rec = recall_score(y_test, y_pred)
        auc = roc_auc_score(y_test, y_prob)

        results[name] = {
            "accuracy": round(acc, 3),
            "recall": round(rec, 3),
            "auc": round(auc, 3)
        }

        print(name, results[name])

    return results


def main():

    evaluate_models()


if __name__ == "__main__":
    main()
