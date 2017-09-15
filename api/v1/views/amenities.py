#!/usr/bin/python3
"""Create a new view for State objects"""
from flask import request, abort
from models import storage, State, Amenity
from api.v1.views import app_views
from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)


@app_views.route('/amenities', strict_slashes=False)
def get_amenities():
    """Retrieves the list of all Amenity objects"""
    amenities_list = []
    for key, value in storage.all("Amenity").items():
        amenities_list.append(value.to_json())
    return (jsonify(amenities_list), 200)


@app_views.route('/amenities/<amenity_id>', strict_slashes=False)
def get_amenity_by_id(amenity_id):
    """Retrieves a Amenity object"""
    amenity = storage.get("Amenity", amenity_id)

    if amenity is None:
        abort(404)
    else:
        amenity = amenity.to_json()
    return (jsonify(amenity), 200)


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_amenity(amenity_id):
    """Deletes amenity by id"""
    empty_dict = {}
    amenity = storage.get("Amenity", amenity_id)

    if amenity is None:
        abort(404)
    else:
        storage.delete(amenity)
        storage.save()
        return jsonify(empty_dict), 200


@app_views.route('/amenities', methods=['POST'],
                 strict_slashes=False)
def create_amenity():
    """Creates a new amenity"""
    req = request.get_json()
    if req is None:
        return (jsonify("Not a JSON"), 400)
    try:
        req["name"]
    except:
        return (jsonify("Missing name"), 400)
    data = Amenity(**req)
    data.save()
    return(jsonify(data.to_json()), 201)


@app_views.route('/amenities/<amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def update_amenity_at_id(amenity_id):
    """Update an amenity at given id"""
    amenity = storage.get("Amenity", amenity_id)
    req = request.get_json()

    if amenity is None:
        abort(404)
    if req is None:
        return (jsonify("Not a JSON"), 400)
    for key, value in req.items():
        setattr(amenity, key, value)
    amenity.save()
    return (jsonify(amenity.to_json()), 200)
