import pandas as pd
import joblib

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# Import hyperparameters from config
from app.core.config import (
    LOGISTIC_PARAMS,
    DECISION_TREE_PARAMS,
    RANDOM_FOREST_PARAMS
)


X_TRAIN_PATH = "data/processed/X_train.csv"
Y_TRAIN_PATH = "data/processed/y_train.csv"
MODEL_DIR = "data/models/"


def train_models():

    print("Loading training data...")

    X_train = pd.read_csv(X_TRAIN_PATH)

    y_train = pd.read_csv(Y_TRAIN_PATH).values.ravel()

    # Initialize models using config hyperparameters
    models = {

        "logistic": LogisticRegression(
            **LOGISTIC_PARAMS
        ),

        "decision_tree": DecisionTreeClassifier(
            **DECISION_TREE_PARAMS
        ),

        "random_forest": RandomForestClassifier(
            **RANDOM_FOREST_PARAMS
        )
    }

    print("Training models...")

    for name, model in models.items():

        model.fit(X_train, y_train)

        path = f"{MODEL_DIR}{name}.pkl"

        joblib.dump(model, path)

        print(f"{name} model trained and saved at {path}")


def main():

    train_models()


if __name__ == "__main__":

    main()
