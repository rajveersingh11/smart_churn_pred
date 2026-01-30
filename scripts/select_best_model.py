import joblib


def select_best():

    # Update after evaluate step
    scores = {
        "logistic": 0.78,
        "decision_tree": 0.74,
        "random_forest": 0.86
    }

    best_model = max(
        scores,
        key=scores.get
    )

    model = joblib.load(
        f"data/models/{best_model}.pkl"
    )

    joblib.dump(
        model,
        "data/models/best_model.pkl"
    )

    print("Best model selected:", best_model)


def main():

    select_best()


if __name__ == "__main__":
    main()
