#!/usr/bin/env python3
"""
function that lists all documents in a collection
"""
import pymongo


def list_all(mongo_collection):
    """
    list all documents
    """
    if not mongo_collection:
        return []
    else:
        return list(mongo_collection.find())
