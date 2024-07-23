from flask import Flask
from routes import scraper_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(scraper_bp)

if __name__ == "__main__":
    app.run(debug=True)
