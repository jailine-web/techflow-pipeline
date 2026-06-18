from src.database import DatabaseConnection
import pytest

def test_database_connect():
    db = DatabaseConnection()
    assert db.connect() == "Connected to database"
    assert db.connected is True


def test_database_query():
    db = DatabaseConnection()
    db.connect()
    result = db.query("SELECT * FROM users")

    assert isinstance(result, list)
    assert result[0]["name"] == "test"


def test_database_disconnect():
    db = DatabaseConnection()
    db.connect()
    db.disconnect()

    assert db.connected is False


def test_query_without_connection():
    db = DatabaseConnection()

    with pytest.raises(ConnectionError):
        db.query("SELECT *")