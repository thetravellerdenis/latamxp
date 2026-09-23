import pytest
from run import app
from app.extensions import db
from models import Usuario


@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()


def test_register_success(client):
    """Test: registro exitoso devuelve 201 y los datos del usuario"""
    response = client.post(
        "/api/v1/auth/register",
        json={
            "nombre": "New User",
            "email": "newuser@example.com",
            "password": "securepassword123",
            "idioma": "en",
        },
    )
    assert response.status_code == 201
    data = response.get_json()
    assert "user" in data
    assert data["user"]["email"] == "newuser@example.com"
    assert "password" not in data["user"]  # La contraseña no debe ser devuelta


def test_register_duplicate_email(client):
    """Test: email duplicado devuelve 400"""
    # Creamos el primer usuario
    client.post(
        "/api/v1/auth/register",
        json={
            "nombre": "User One",
            "email": "duplicate@example.com",
            "password": "password123",
        },
    )

    # Intentamos crear un segundo con el mismo email
    response = client.post(
        "/api/v1/auth/register",
        json={
            "nombre": "User Two",
            "email": "duplicate@example.com",
            "password": "password123",
        },
    )
    assert response.status_code == 400
    data = response.get_json()
    assert "errors" in data
    assert "email" in data["errors"]


def test_register_short_password(client):
    """Test: contraseña corta devuelve 400"""
    response = client.post(
        "/api/v1/auth/register",
        json={
            "nombre": "Short Pass",
            "email": "short@example.com",
            "password": "123",  # Menos de 8 caracteres
        },
    )
    assert response.status_code == 400
    data = response.get_json()
    assert "errors" in data
    assert "password" in data["errors"]


def test_register_invalid_email(client):
    """Test: formato de email inválido devuelve 400"""
    response = client.post(
        "/api/v1/auth/register",
        json={
            "nombre": "Bad Email",
            "email": "not-an-email",
            "password": "password123",
        },
    )
    assert response.status_code == 400
    data = response.get_json()
    assert "errors" in data
    assert "email" in data["errors"]
