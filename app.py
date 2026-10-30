import os
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from guide_service import GuideError, generate_guide

load_dotenv()
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 4096

@app.get('/')
def index():
    return render_template('index.html')

@app.post('/api/generate')
def generate():
    data = request.get_json(silent=True)
    subject = data.get('app') if isinstance(data, dict) else None
    if not isinstance(subject, str) or not subject.strip() or len(subject.strip()) > 200:
        return jsonify(error='Enter an app name or website (up to 200 characters).'), 400
    key = os.getenv('GEMINI_API_KEY', '').strip()
    if not key:
        return jsonify(error='Add GEMINI_API_KEY to your .env file and restart the server.'), 503
    try:
        return jsonify(generate_guide(subject.strip(), key))
    except GuideError as exc:
        return jsonify(error=str(exc)), exc.status
