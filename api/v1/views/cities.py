#!/usr/bin/python3
"""Creates a new view for City objects"""
from flask import request, abort
from models import storage
from api.v1.views import app_views
from flask import Flask, render_template, jsonify
import json
from models import State, City

app = Flask(__name__)


@app_views.route('/states/cities', methods=['GET'], strict_slashes=False)
def all_cities():
    """Retrieves list of all City objects"""

    all_list = []

    for k, v in storage.all("City").items():
        all_list.append(v.to_json())
    return (jsonify(all_list))


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def cities_by_state(state_id):
    """Retrieves list of all City objects"""

    all_list = []
    city_list = []
    state = storage.get("State", state_id)

    if state is None:
        abort(404)

    for k, v in storage.all("City").items():
        all_list.append(v.to_json())

    for city in all_list:
        if city['state_id'] == state_id:
            city_list.append(city)

    return (jsonify(city_list))


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_city(city_id):
    """Retrieves City object"""
    city = storage.get("City", city_id)

    if city is None:
        abort(404)

    return (jsonify(city.to_json()))


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_city(city_id):
    """Deletes a City object"""
    empty_dict = {}

    city = storage.get("City", city_id)

    if city is None:
        abort(404)

    else:
        storage.delete(city)
        storage.save()
        return jsonify(empty_dict), 200


@app_views.route('/states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def add_city(state_id):
    """Creates City object"""
    req = request.get_json()

    state = storage.get("State", state_id)

    if state is None:
        abort(404)

    if req is None:
        return (jsonify("Not a JSON"), 400)

    try:
        req['name']
    except:
        return (jsonify("Missing name"), 400)

    req['state_id'] = state_id
    city_data = City(**req)

    for k, v in req.items():
        setattr(city_data, k, v)

    city_data.save()
    return (jsonify(city_data.to_json()), 201)

@app_views.route('/cities/<city_id>', methods=['PUT'],
                 strict_slashes=False)
def update_city(city_id):
    """Updates City object"""
    city = storage.get("City", city_id)
    req = request.get_json()

    if city is None:
        abort(404)

    if req is None:
        return(jsonify("Not a JSON"), 400)

    for k, v in req.items():
        setattr(city, k, v)

    city.save()

    return (jsonify(city.to_json()), 200)
