#!/usr/bin/python3
"""Create a new view for State objects"""
from flask import request, abort
from models import storage, Review
from api.v1.views import app_views
from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)


@app_views.route('/places/<place_id>/reviews', methods=['GET'],
                 strict_slashes=False)
def reviews_by_place(place_id):
    """Retrieves the list of all Review objects of a Place"""
    all_list = []
    review_list = []
    place = storage.get("Place", place_id)

    if place is None:
        abort(404)

    for key, value in storage.all("Place").items():
        all_list.append(v.to_json())

    for review in all_list:
        if review['place_id'] == place.id:
            review_list.append(review)

    return (jsonify(review_list), 200)


@app_views.route('/reviews/<review_id>', methods=['GET'],
                 strict_slashes=False)
def get_review_object(review_id):
    """Retrieves a Review object"""
    review = storage.get("Review", review_id)

    if review is None:
        abort(404)

    return (jsonify(review.to_json()), 200)


@app_views.route('/reviews/<review_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_review(review_id):
    """Deletes a review by its id"""
    empty_dict = {}

    review = storage.get("Review", review_id)

    if review is None:
        abort(404)
    else:
        storage.delete(review)
        storage.save()
        return (jsonify(empty_dict), 200)


@app_views.route('/places/<place_id>/reviews', methods=['POST'],
                 strict_slashes=False)
def create_review(place_id):
    """Creates a new review"""
    req = request.get_json()

    place = storage.get("Place", place_id)

    if place is None:
        abort(404)

    if req is None:
        return (jsonify("Not a JSON"), 400)

    try:
        req['user_id']
    except:
        return (jsonify("Missing user_id"), 400)

    try:
        req['text']
    except:
        return (jsonify("Missing text"), 400)

    req['place_id'] = place_id
    review_data = Review(**req)

    for key, value in req.items():
        setattr(review_data, key, value)

    review_data.save()
    return (jsonify(review_data.to_json()), 201)


@app_views.route('/reviews/<review_id>', methods=['PUT'],
                 strict_slashes=False)
def update_review(review_id):
    """Updates Review object"""
    review = storage.get("Review", review_id)
    req = request.get_json()

    if review is None:
        abort(404)
    if req is None:
        return(jsonify("Not a JSON"), 400)

    for key, value in req.items():
        setattr(review, key, value)

    review.save()

    return (jsonify(review.to_json()), 200)
