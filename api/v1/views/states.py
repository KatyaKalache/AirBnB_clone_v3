#!/usr/bin/python3
"""Create a new view for State objects"""
from flask import request, abort
from models import storage
from api.v1.views import app_views
from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app_views.route('/states', strict_slashes=False)
def get_state():
    """Retrives the list of all State objects"""
    all_list = []
    for key, value in storage.all("State").items():
        all_list.append(value.to_json())
    return (jsonify(all_list))


@app_views.route('/states/<state_id>', strict_slashes=False)
def get_id(state_id):
    """Retrieves a State object"""
    id_list = []

    state = storage.get("State", state_id)

    if state is None:
        abort(404)
    else:
        id_list.append(state.to_json())
    return (jsonify(id_list))


@app_views.route('/states/<state_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """Deletes a State object"""
    empty_dict = {}

    state = storage.get("State", state_id)

    if state is None:
        abort(404)

    else:
        storage.delete(state)
        storage.save()
        return jsonify(empty_dict), 200
