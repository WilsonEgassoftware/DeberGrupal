"""
frontend-service  (SERVICIO PÚBLICO - VULNERABLE A PROPÓSITO)
Laboratorio académico ITIZ2302. NO usar en producción.
"""
import logging
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s [frontend] %(message)s")


@app.get("/")
def index():
    return jsonify(
        service="frontend-service",
        endpoints=["/health", "/preview?url=<URL>"],
        note="Servicio vulnerable a propósito (laboratorio SSRF)",
    )


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/preview")
def preview():
    url = request.args.get("url")
    if not url:
        return jsonify(error="Falta el parámetro 'url'"), 400

    app.logger.info("Petición saliente hacia: %s", url)

    # VULNERABLE A PROPÓSITO (CWE-918): la URL del usuario se usa tal cual,
    # sin allowlist ni bloqueo de rangos internos. P4 lo corrige en /hardening.
    try:
        r = requests.get(url, timeout=5)
        return r.text, r.status_code, {"Content-Type": r.headers.get("Content-Type", "text/plain")}
    except requests.RequestException as e:
        return jsonify(error=str(e)), 502


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
