import pytest
from src.database import DatabaseConnection

def test_query_without_connection():
    db = DatabaseConnection()

    with pytest.raises(ConnectionError):
        db.query("SELECT * FROM users")