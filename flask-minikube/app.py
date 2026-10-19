import os

from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)
    message = os.environ.get("APP_MESSAGE", "Hello from Flask on Minikube!")

    @app.get("/")
    def home():
        return jsonify(message=message)

    @app.get("/health")
    def health():
        return jsonify(status="ok")

    return app


app = create_app()
