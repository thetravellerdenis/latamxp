from flask import Blueprint, jsonify, request
from models import db, Usuario
from app.schemas.auth import UsuarioRegisterSchema
from werkzeug.security import generate_password_hash
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required, get_jwt_identity

auth_api_bp = Blueprint("auth_api", __name__, url_prefix="/api/v1/auth")


@auth_api_bp.route("/register", methods=["POST"])
def api_register():
    # Получаем JSON данные
    json_data = request.get_json()
    if not json_data:
        return jsonify({"error": "No input data provided"}), 400

    # Валидация через Marshmallow
    schema = UsuarioRegisterSchema()
    try:
        data = schema.load(json_data)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    # Проверка, существует ли пользователь с таким email
    email = data.get("email")
    existing_user = Usuario.query.filter_by(email=email).first()
    if existing_user:
        return (
            jsonify({"errors": {"email": ["This email is already registered."]}}),
            400,
        )

    # Создание нового пользователя
    new_user = Usuario(
        nombre=data.get("nombre"),
        email=email,
        idioma_preferido=data.get("idioma", "es"),
    )

    # Хеширование пароля
    new_user.set_password(data.get("password"))

    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Database error. Could not create user."}), 500

    # Возвращаем 201 Created с данными пользователя
    return (
        jsonify({"message": "User created successfully.", "user": new_user.to_dict()}),
        201,
    )


@auth_api_bp.route("/me", methods=["GET"])
@jwt_required()
def api_me():
    # 1. Extraer user_id del token
    current_user_id = get_jwt_identity()

    # 2. Buscar usuario en DB
    user = db.session.get(Usuario, int(current_user_id))

    if not user:
        return jsonify({"msg": "User not found"}), 404

    # 3. Retornar 200 con datos
    return (
        jsonify({"id": user.id_usuario, "nombre": user.nombre, "email": user.email}),
        200,
    )
