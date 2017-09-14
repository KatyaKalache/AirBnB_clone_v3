#!/usr/bin/python3
"""Create a new view for State objects"""
from flask import request
from models import storage
from api.v1.views import app_views
from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app_views.route('/states', strict_slashes=False)
def get_state():
    all_list = []
    for key, value in storage.all("State").items():
        all_list.append(value.to_json())
    return(jsonify(all_list))
