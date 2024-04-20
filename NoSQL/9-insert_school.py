#!/usr/bin/env python3
"""
function that inserts a new document in a collection based on kwargs
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
     inserts a new document in collection
    """
    document = mongo_collection.insert(kwargs)
    return document.inserted_id
