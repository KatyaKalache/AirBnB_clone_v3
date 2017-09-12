#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage

print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count("State")))

first_state_id = list(storage.all("State").keys())[0]
print("First state: {}".format(storage.get("State", first_state_id)))
