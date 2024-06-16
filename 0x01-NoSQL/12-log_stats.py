#!/usr/bin/env python3

"""
This module provides functions to retrieve and display
log statistics from a MongoDB collection.

Author: Komlanvi Fabrice Eklou
Date: 2024-06-16
"""


def get_stats(logs_collection):
    """
    Retrieve log statistics from the given MongoDB collection
    and display them.

    Args:
        logs_collection (pymongo.collection.Collection): The MongoDB
            collection containing the logs.

    Returns:
        None
    """
    logs_count = logs_collection.count_documents({})
    gets = logs_collection.count_documents({'method': 'GET'})
    posts = logs_collection.count_documents({'method': 'POST'})
    puts = logs_collection.count_documents({'method': 'PUT'})
    patchs = logs_collection.count_documents({'method': 'PATCH'})
    deletes = logs_collection.count_documents({'method': 'DELETE'})
    status_check = logs_collection.count_documents({'path': '/status'})

    methods_counts = [('GET', gets), ('POST', posts),
                      ('PUT', puts), ('PATCH', patchs),
                      ('DELETE', deletes)]

    print("{} logs".format(logs_count))

    print("Methods:")
    for method, count in methods_counts:
        print("    method {}: {}".format(method, count))

    print("{} status check".format(status_check))


if __name__ == '__main__':
    from pymongo import MongoClient

    client = MongoClient('localhost', 27017)
    logs_collection = client.logs.nginx

    get_stats(logs_collection)
