#!/usr/bin/python3
"""Creates a new view for Place objects"""
from flask import request, abort
from models import storage, Place, State, User
from api.v1.views import app_views
from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)


@app_views.route('/cities/<city_id>/places', methods=['GET'],
                 strict_slashes=False)
def all_places(city_id):
    """Retrieves list of all Place objects"""
    all_places = []
    result_list = []

    city = storage.get("City", city_id)

    if city is None:
        abort(404)

    for k, v in storage.all("Place").items():
        all_places.append(v.to_json())

    for place in all_places:
        if place['city_id'] == city_id:
            result_list.append(place)

    return (jsonify(result_list))


@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def get_place(place_id):
    """Retrieves a Place object based on its place_id"""
    place = storage.get("Place", place_id)

    if place is None:
        abort(404)

    return (jsonify(place.to_json()))


@app_views.route('/places/<place_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_place(place_id):
    """Deletes a Place object"""
    empty_dict = {}

    place = storage.get("Place", place_id)

    if place is None:
        abort(404)

    else:
        storage.delete(place)
        storage.save()
        return jsonify(empty_dict), 200


@app_views.route('/cities/<city_id>/places', methods=['POST'],
                 strict_slashes=False)
def create_place(city_id):
    """Creates a Place object"""
    req = request.get_json()

    place = storage.get("City", city_id)

    if place is None:
        abort(404)

    if req is None:
        return (jsonify("Not a JSON"), 400)

    try:
        req['user_id']
    except:
        return (jsonify("Missing user_id"), 400)

    try:
        req['name']
    except:
        return (jsonify("Missing name"), 400)

    user = storage.get("User", req['user_id'])

    if user is None:
        abort(404)

    req['city_id'] = city_id
    user_data = User(**req)

    for k, v in req.items():
        setattr(user_data, k, v)

    user_data.save()

    return (jsonify(user_data.to_json()), 201)


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def update_place(place_id):
    """Updates a Place object"""
    place = storage.get("Place", place_id)
    req = request.get_json()

    if place is None:
        abort(404)

    if req is None:
        return(jsonify("Not a JSON"), 400)

    for k, v in req.items():
        setattr(place, k, v)

    place.save()

    return (jsonify(place.to_json()), 200)
