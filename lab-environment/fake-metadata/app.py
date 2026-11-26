"""
fake-metadata  (SIMULA el servicio de metadata de AWS - TODO ES FICTICIO)
Imita la estructura de http://169.254.169.254/latest/meta-data/ sin tocar infraestructura real.
"""
import logging
from flask import Flask, request, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s [fake-metadata] %(message)s")

ROLE = "lab-ec2-role"


@app.before_request
def log_request():
    app.logger.info("%s %s desde %s", request.method, request.path, request.remote_addr)


@app.get("/latest/meta-data/")
def root():
    return "ami-id\ninstance-id\niam/\n", 200, {"Content-Type": "text/plain"}


@app.get("/latest/meta-data/instance-id")
def instance_id():
    return "i-0fake000000000000", 200, {"Content-Type": "text/plain"}


@app.get("/latest/meta-data/iam/security-credentials/")
def roles():
    return ROLE, 200, {"Content-Type": "text/plain"}


@app.get(f"/latest/meta-data/iam/security-credentials/{ROLE}")
def creds():
    return jsonify(
        Code="Success",
        Type="AWS-HMAC",
        AccessKeyId="AKIAFAKEFAKEFAKEFAKE",
        SecretAccessKey="FAKE/secret/access/key/for/lab/only",
        Token="FAKE-SESSION-TOKEN-LAB-ONLY",
        Expiration="2099-12-31T23:59:59Z",
    )


@app.get("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
