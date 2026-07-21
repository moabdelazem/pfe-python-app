from flask import Blueprint, jsonify
import datetime
import socket

api_bp = Blueprint("api", __name__)

@api_bp.route("/info")
def info():
    return jsonify({
        "time": datetime.datetime.now().strftime("%I:%M:%S %p on %B %d, %Y"),
        "hostname": socket.gethostname(),
        "message": "Hooray it's Working!",
    })

@api_bp.route("/healthz")
def health():
    return jsonify({"status": "up", "version": "0.0.1", "service": "python-flask-app"}), 200