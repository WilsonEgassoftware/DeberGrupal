"""
internal-admin-service  (SERVICIO INTERNO)
Solo debería ser alcanzable dentro de internal-net. Datos 100% ficticios.
"""
import logging
from flask import Flask, request, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s [internal-admin] %(message)s")


@app.before_request
def log_request():
    app.logger.info("%s %s desde %s", request.method, request.path, request.remote_addr)


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/")
def index():
    return jsonify(service="internal-admin-service", endpoints=["/admin/users", "/admin/config"])


@app.get("/admin/users")
def users():
    return jsonify(users=[
        {"id": 1, "user": "admin", "role": "superadmin"},
        {"id": 2, "user": "maria.lopez", "role": "finance"},
        {"id": 3, "user": "jperez", "role": "support"},
    ])


@app.get("/admin/config")
def config():
    return jsonify(
        db_host="db.internal.lab",
        db_password="FAKE-PASSWORD-123",   # ficticio
        api_key="FAKE-INTERNAL-API-KEY",   # ficticio
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
