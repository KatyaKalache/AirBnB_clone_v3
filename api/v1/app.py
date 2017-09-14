#!/usr/bin/python3
"""returns a JSON-formatted 404 status code response"""
from flask import Flask, Blueprint, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def shutdown(self):
    """teardown hander"""
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error="Not found")

if __name__ == "__main__":
    app.run(host=getenv('HBNB_API_HOST'), port=getenv('HBNB_API_PORT'))
