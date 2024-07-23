import os
from flask import Blueprint, request, jsonify, send_file
from generate_podcast import generate_podcast

scraper_bp = Blueprint('scraper', __name__)

@scraper_bp.route('/g1', methods=['POST'])
def scrape():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400

    try:
        history, file_path = generate_podcast(url)
        if not os.path.exists(file_path):
            return jsonify({"error": "File not found"}), 404
        return send_file(file_path, as_attachment=True, mimetype="audio/wav"), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500