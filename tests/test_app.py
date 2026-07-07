from fastapi.testclient import TestClient

from backend.app import app


client = TestClient(app)


def test_health_endpoint_returns_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_root_endpoint_returns_welcome_message():
    response = client.get("/")
    assert response.status_code == 200
    assert "Agentic Graph RAG AI Knowledge Assistant" in response.json()["message"]
