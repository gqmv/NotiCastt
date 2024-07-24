from flask import Flask
from flask_cors import CORS
from routes import scraper_bp

app = Flask(__name__)
CORS(app)
app.register_blueprint(scraper_bp)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
