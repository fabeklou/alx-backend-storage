#!/usr/bin/env python3

"""
This module provides a function to retrieve the top 10 students
based on their average score.
"""


def top_students(mongo_collection):
    """
    Retrieve the top 10 students based on their average score.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB
            collection containing student data.

    Returns:
        list: A list of the top 10 students, sorted by their average score.
    """
    aggregation_pipeline = [
        {"$addFields": {"averageScore": {"$avg": "$topics.score"}}},
        {"$sort": {"averageScore": -1}},
        {"$limit": 10}
    ]
    top_ten = mongo_collection.aggregate(aggregation_pipeline)
    return list(top_ten)
