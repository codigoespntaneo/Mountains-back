from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_mountain_and_returns_200():
    response = client.post(
        "/mountains/",
        json={
            "name": "Monte Everest",
            "country": "Nepal / China",
            "height": 8849,
            "img": "https://example.com/everest.jpg"
        }
    )
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["name"] == "Monte Everest"
    assert response.json()["country"] == "Nepal / China"
    assert response.json()["height"] == 8849
    assert response.json()["img"] == "https://example.com/everest.jpg"