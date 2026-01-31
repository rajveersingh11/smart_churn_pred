def get_token(client):

    res = client.post(
        "/auth/login",
        json={
            "username": "admin",
            "password": "admin"
        }
    )

    return res.json()["access_token"]

def test_predict(client):

    token = get_token(client)

    res = client.post(
        "/churn/predict",
        headers={"token": token},
        json={
            "features": [1, 1, 0.3, 200, 80, 2]
        }
    )

    assert res.status_code == 200

    data = res.json()
    assert "churn_probability" in data
    assert "risk_level" in data
    assert "recommended_action" in data