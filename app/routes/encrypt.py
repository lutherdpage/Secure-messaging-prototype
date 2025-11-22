from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

encrypt_bp = Blueprint("encrypt", __name__, url_prefix="/encrypt")

# Example protected route
@encrypt_bp.get("/secure")
@jwt_required()
def secure_endpoint():
    current_user = get_jwt_identity()
    return jsonify({
        "msg": "You accessed a protected route",
        "user": current_user
    })

# Example encryption route (stubbed)
@encrypt_bp.post("/text")
@jwt_required()
def encrypt_text():
    data = request.get_json()
    plaintext = data.get("message")

    if not plaintext:
        return jsonify({"error": "No message provided"}), 400

    # TODO: replace with real encryption logic
    ciphertext = plaintext[::-1]  # simple reversal for demo

    return jsonify({
        "user": get_jwt_identity(),
        "ciphertext": ciphertext
    })