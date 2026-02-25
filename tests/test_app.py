import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

# AAA: Arrange-Act-Assert

def test_root_endpoint():
    # Arrange
    url = "/"
    # Act
    response = client.get(url)
    # Assert
    assert response.status_code == 200
    assert "Hello" in response.text
