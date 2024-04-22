#!/usr/bin/env python3
"""
script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient

if __name__ == "__main__":

    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    documents = collection.count_documents({})
    print(f"{documents} logs")

    METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print("Methods:")
    for method in METHODS:
        documents = collection.find({"method": method})
        numero_documents = documents.count()
        print(f"\tmethod {method}: {numero_documents}")

    cont_docs = collection.find({
        "method": "GET",
        "path": "/status"
    })

    print(f"{cont_docs} status check")
