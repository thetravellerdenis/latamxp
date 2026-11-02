from functools import wraps
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from models import Usuario # Импортируем модель

def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            # Проверяем наличие и валидность токена
            verify_jwt_in_request()
            
            # Получаем ID юзера из токена
            user_id = get_jwt_identity()
            user = Usuario.query.get(int(user_id)) # Ищем в базе
            
            # Проверяем, админ ли он
            if not user or not getattr(user, 'is_admin', False):
                return jsonify(msg="Admins only!"), 403
                
            return fn(*args, **kwargs)
        return decorator
    return wrapper