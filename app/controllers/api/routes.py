from flask import Blueprint, jsonify, request
from models import db, Tour, Usuario
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
)

api_bp = Blueprint("api", __name__, url_prefix="/api/v1")


@api_bp.route("/tours", methods=["GET"])
def get_tours():
    tours = Tour.query.filter_by(activo=True).all()
    return jsonify({"data": [t.to_dict() for t in tours]})


@api_bp.route("/tours/<int:tour_id>", methods=["GET"])
def get_tour(tour_id):
    tour = db.get_or_404(Tour, tour_id)
    return jsonify({"data": tour.to_dict()})


@api_bp.route("/auth/login", methods=["POST"])
def api_login():
    data = request.get_json()
    user = Usuario.query.filter_by(email=data.get("email")).first()

    if user and user.check_password(data.get("password")):
        access_token = create_access_token(identity=str(user.id_usuario))
        refresh_token = create_refresh_token(identity=str(user.id_usuario))

        return (
            jsonify(
                {
                    "status": "success",
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "user": user.to_dict(),
                }
            ),
            200,
        )

    return jsonify({"status": "error", "message": "Invalid credentials"}), 401


@api_bp.route("/auth/refresh", methods=["POST"])
@jwt_required(refresh=True)
def api_refresh():
    current_user_id = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user_id)
    return jsonify({"access_token": new_access_token}), 200


@api_bp.route("/test-protected", methods=["GET"])
@jwt_required()
def test_protected():
    current_user_id = get_jwt_identity()
    return (
        jsonify({"message": f"Hello user {current_user_id}! You have a valid token."}),
        200,
    )
