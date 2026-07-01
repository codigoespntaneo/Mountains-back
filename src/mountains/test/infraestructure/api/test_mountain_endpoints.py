from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_all_mountains_returns_list():
    response = client.get("/mountains/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_mountain_by_id_returns_200():

    create = client.post(
        "/mountains/",
        json={
            "name": "Monte Everest",
            "country": "Nepal / China",
            "height": 8849,
            "img": "https://example.com/everest.jpg"
        },
    )
    mountain_id = create.json()["id"]

    response = client.get(f"/mountains/{mountain_id}")
    assert response.status_code == 200
    assert response.json()["id"] == mountain_id
    assert response.json()["name"] == "Monte Everest"
    assert response.json()["country"] == "Nepal / China"
    assert response.json()["height"] == 8849
    assert response.json()["img"] == "https://example.com/everest.jpg"


def test_get_mountain_by_id_not_found():
    response = client.get("/mountains/999999")
    assert response.status_code == 404


def test_update_mountain_returns_200():
    create = client.post(
        "/mountains/",
        json={
            "name": "Monte Everest",
            "country": "Nepal / China",
            "height": 8849,
            "img": "https://example.com/everest.jpg"
        }
    )
    mountain_id = create.json()["id"]

    response = client.put(
        f"/mountains/{mountain_id}",
        json={
            "name": "Monte Everest",
            "country": "Nepal / China",
            "height": 8849,
            "img": "https://example.com/everest-v2.jpg"
        },
    )
    assert response.status_code == 200
    assert response.json()["country"] == "Nepal / China"
    assert response.json()["height"] == 8849
    assert response.json()["img"] == "https://example.com/everest-v2.jpg"


def test_update_mountain_not_found():
    response = client.put(
        "/mountains/999999",
        json={
            "name": "Monte Everest",
            "country": "Nepal / China",
            "height": 8849,
            "img": "https://example.com/everest.jpg"
        },
    )
    assert response.status_code == 404


def test_delete_mountain_returns_200():
    create = client.post(
        "/mountains/",
        json={
            "name": "Monte Everest",
            "country": "Nepal / China",
            "height": 8849,
            "img": "https://example.com/everest.jpg"
        }
    )
    mountain_id = create.json()["id"]

    response = client.delete(f"/mountains/{mountain_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Mountain deleted successfully"


def test_delete_mountain_not_found():
    response = client.delete("/mountains/999999")
    assert response.status_code == 404