import os

def test_model_exists():

    assert os.path.exists(
        "data/models/best_model.pkl"
    )