from src.database import DatabaseConnection

def test_database_connect():
    db = DatabaseConnection()
    assert db.connect() == "Connected to database"
    assert db.connected is True

def test_database_query():
    db = DatabaseConnection()
    db.connect()
    result = db.query("SELECT * FROM users")
    assert isinstance(result, list)