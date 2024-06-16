#!/usr/bin/env python3

"""
This module provides a function to retrieve a list
of schools that match a given topic.
"""


def schools_by_topic(school_collection, topic):
    """
    Retrieve a list of schools that match a given topic.

    Args:
        school_collection (collection): The collection of school
            documents.
        topic (str): The topic to search for in topics field.

    Returns:
        list: A list of schools that match the given topic.
    """
    schools = school_collection.find({"topics": topic})
    return list(schools)
