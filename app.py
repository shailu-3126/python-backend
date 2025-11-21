from flask import Flask, jsonify
import os
from dotenv import load_dotenv

# Load values from .env (created during deployment)
load_dotenv()

app = Flask(__name__)

DB_URL = os.getenv("DB_URL")
EXTERNAL_API_KEY = os.getenv("EXTERNAL_API_KEY")


@app.route("/")
def index():
    return jsonify(
        status="ok",
        db_url_configured=bool(DB_URL),
        external_api_configured=bool(EXTERNAL_API_KEY),
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
