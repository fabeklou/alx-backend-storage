#!/usr/bin/env python3

"""
This module provides a function to update the topics field
of a document in a MongoDB collection.
"""


def update_topics(mongo_collection, name, topics):
    """
    Update the topics field of a document in the given MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB
            collection to update.
        name (str): The name of the document to update.
        topics (list): The new list of topics to set for the document.

    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
