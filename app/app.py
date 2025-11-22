from flask import Flask
from flask_jwt_extended import JWTManager
from app.routes import encrypt_bp, auth_bp

def create_app():
    app = Flask(__name__)

    # Configure JWT secret key (use env var in production!)
    app.config["JWT_SECRET_KEY"] = "super-secret-key"

    # Initialize JWT
    jwt = JWTManager(app)

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(encrypt_bp)

    @app.get("/health")
    def health():
        return {"status": "healthy"}

    @app.get("/")
    def root():
        return {"message": "Secure Messaging API Running"}

    return app