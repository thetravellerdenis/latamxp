import pytest
from run import app
from app.extensions import db
from models import Usuario

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:' # Тестовая БД в памяти
    with app.app_context():
        db.create_all()
        # Создаем тестового юзера
        u = Usuario(nombre="Test", email="api@test.com")
        u.set_password("password123")
        db.session.add(u)
        db.session.commit()
        
        with app.test_client() as client:
            yield client
            
        db.session.remove()
        db.drop_all()

def test_login_success(client):
    """Тест: успешный логин возвращает токены и expires_in"""
    response = client.post('/api/v1/auth/login', json={
        "email": "api@test.com",
        "password": "password123"
    })
    assert response.status_code == 200
    data = response.get_json()
    assert "access_token" in data
    assert "refresh_token" in data
    assert "expires_in" in data
    assert data["expires_in"] == 3600

def test_login_invalid_password(client):
    """Тест: неверный пароль возвращает 401"""
    response = client.post('/api/v1/auth/login', json={
        "email": "api@test.com",
        "password": "wrongpassword"
    })
    assert response.status_code == 401
    assert response.get_json()["message"] == "Invalid credentials"

def test_login_inactive_user(client):
    """Тест: заблокированный юзер получает 403"""
    # Делаем юзера неактивным
    u = Usuario.query.filter_by(email="api@test.com").first()
    u.activo = False
    db.session.commit()

    response = client.post('/api/v1/auth/login', json={
        "email": "api@test.com",
        "password": "password123"
    })
    assert response.status_code == 403
    assert response.get_json()["message"] == "Account is deactivated"