#!/usr/bin/env python3

"""This module contains a function to retrieve all documents
from the given MongoDB collection.
"""


def list_all(mongo_collection):
    """
    Retrieve all documents from the given MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB
            collection to retrieve documents from.

    Returns:
        list: A list of all documents retrieved from the collection.
    """
    documents = mongo_collection.find()
    return list(documents)
