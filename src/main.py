from flask import Flask 
from .routes import api_bp

app = Flask(__name__)

app.register_blueprint(api_bp, url_prefix="/api/v1")

@app.errorhandler(404)
def not_found(error):
    return {
        "error": "Not Found"
    }, 404


@app.errorhandler(500)
def internal(error):
    return {
        "error": "Internal Server Error"
    }, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0")