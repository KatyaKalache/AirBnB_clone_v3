#!/usr/bin/python3
"""Creates a new view for User objects"""
from flask import request, abort
from models import storage
from api.v1.views import app_views
from flask import Flask, render_template, jsonify
import json
from models import State

app = Flask(__name__)


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """Retrieves a list of all User objects"""
    all_list = []
    for k, v in storage.all("User").items():
        all_list.append(value.to_json())
    return (jsonify(all_list))


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user_by_id():
    """Retrieves a User object using user_id"""
    user = storage.get("User", user_id)

    if user is None:
        abort(404)

    else:
        user = [user.to_json()]
    return (jsonify(user))


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """Deletes a User object"""
    empty_dict = {}

    user = storage.get("User", user_id)

    if user is None:
        abort(404)

    else:
        storage.delete(user)
        storage.save()
        return jsonify(empty_dict), 200


@app_views.route('/v1/users', methods=['POST'], strict_slashes=False)
def create_user():
    """Creates a User object"""
    req = request.get_json()

    if req is None:
        return (jsonify("Not a JSON"), 400)

    try:
        req['email']
    except:
        return (jsonify("Missing email"), 400)

    try:
        req['password']
    except:
        return (jsonify("Missing password"), 400)

    data = State(**req)
    data.save()

    return (jsonify(data.to_json()), 201)


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """Updates a User object"""
    user = storage.get("User", user_id)
    req = request.get_json()

    if user is None:
        abort(404)

    if req is None:
        return (jsonify("Not a JSON"), 400)

    for k, v in req.items():
        setattr(user, k, v)

    user.save()

    return (jsonify(user.to_json()), 200)
