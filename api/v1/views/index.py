#!/usr/bin/python3
from api.v1.views import app_views
from flask import Flask, render_template, jsonify
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False

class_dict = {
    'Amenity': 'amenities',
    'City': 'cities',
    'Place': 'places',
    'Review': 'reviews',
    'State': 'states',
    'User': 'users'
    }


@app_views.route('/status')
def json_status():
    """Returns JSON status"""
    return jsonify(status="OK")


@app_views.route('/stats')
def example():
    """Retrieves number of each objects by type"""
    count_dict = {}
    for key, value in class_dict.items():
        count_dict[value] = storage.count(key)
    return jsonify(count_dict)
