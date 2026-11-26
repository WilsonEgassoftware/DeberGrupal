import ssl
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/status", methods=["GET"])
def status():
    return jsonify({
        "service": "internal-admin-service",
        "status": "operational",
        "auth": "mTLS verified"
    }), 200

@app.route("/admin/secrets", methods=["GET"])
def admin_secrets():
    return jsonify({
        "admin_token": "REDACTED_HARDENED_SECRET",
        "message": "Acceso concedido únicamente vía mTLS verificado"
    }), 200

if __name__ == "__main__":
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    context.load_cert_chain(
        certfile="/app/certs/server.crt",
        keyfile="/app/certs/server.key"
    )
    context.load_verify_locations(cafile="/app/certs/ca.crt")
    context.verify_mode = ssl.CERT_REQUIRED

    app.run(host="0.0.0.0", port=8443, ssl_context=context)
