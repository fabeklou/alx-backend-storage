#!/usr/bin/env python3

"""
This module provides a function to insert a school document
into a MongoDB collection.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a school document into the specified MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB
            collection to insert the document into.
        **kwargs: Keyword arguments representing the fields
            and values of the school document.

    Returns:
        str: The document ID of the inserted school document.
    """
    document_id = mongo_collection.insert({**kwargs})
    return document_id
