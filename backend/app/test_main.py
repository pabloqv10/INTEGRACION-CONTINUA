import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch
from main import app

# Establecer entorno de prueba antes de cargar el app
import os
os.environ["TEST_ENV"] = "true"

client = TestClient(app)

@pytest.fixture
def mock_db_connection():
    with patch("main.get_db_connection") as mock_get_db_connection:
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_get_db_connection.return_value = mock_conn
        yield mock_conn, mock_cursor

# Prueba de ejemplo: Hello World
def test_say_hello():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}
