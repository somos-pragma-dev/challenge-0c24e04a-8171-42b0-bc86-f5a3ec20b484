from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_create_transaction():
    response = client.post(
        "/transactions/",
        json={"amount": 100, "status": "pending"},
    )
    assert response.status_code == 200
    assert response.json().get('amount') == 100


def test_read_transaction():
    response = client.get("/transactions/1")
    assert response.status_code == 200
    assert response.json().get('amount') == 100


def test_read_transactions():
    response = client.get("/transactions/")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_update_transaction():
    response = client.put(
        "/transactions/1",
        json={"amount": 200, "status": "completed"},
    )
    assert response.status_code == 200
    assert response.json().get('amount') == 200


def test_delete_transaction():
    response = client.delete("/transactions/1")
    assert response.status_code == 200
    assert response.json().get('detail') == 'Transaction deleted'