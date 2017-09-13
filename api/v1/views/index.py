#!/usr/bin/python3
from api.v1.views import app_views
from flask import Flask, render_template, jsonify
app = Flask(__name__)
app.url_map.strict_slashes = False

@app_views.route('/status')
def json_status():
    """Returns JSON status"""
    return jsonify(status="OK")
