# app/utils/auth_middleware.py
from flask import request, jsonify
import jwt
from functools import wraps

from app.routes.auth import jwt_secret, JWT_ALGO

def require_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"error": "Missing or invalid Authorization header"}), 401

        token = auth_header.split(" ")[1]

        try:
            payload = jwt.decode(token, jwt_secret, algorithms=[JWT_ALGO])
            request.user = payload["sub"]
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expired"}), 401
        except Exception:
            return jsonify({"error": "Invalid token"}), 401

        return f(*args, **kwargs)
    return wrapper
