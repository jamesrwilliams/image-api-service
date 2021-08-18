from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/api/")
def api_page():
    return jsonify({
        'error': 'JSON'
    })
