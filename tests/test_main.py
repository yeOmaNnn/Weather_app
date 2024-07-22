from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_weather():
    response = client.post("/weather", json={"city": "London"})
    assert response.status_code == 200
    assert response.json()["city"] == "London"
