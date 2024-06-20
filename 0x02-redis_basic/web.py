#!/usr/bin/env python3

"""
This module provides a caching mechanism for web pages using Redis.
"""


import requests
import redis
from typing import Callable
import functools

redis_client = redis.Redis()


def cache_page(method: Callable) -> Callable:
    """
    Decorator function that caches the page content
    and counts the number of accesses.

    Args:
        method (Callable): The original function that
            fetches the page content.

    Returns:
        Callable: The decorated function that caches the page
            content and counts the number of accesses.
    """

    @functools.wraps(method)
    def wrapper(url: str) -> str:
        """
        Wrapper function that caches the page content and counts
        the number of accesses.

        Args:
            url (str): The URL of the page to fetch.

        Returns:
            str: The content of the page.
        """
        # Generate cache key and count key
        cache_key = "cache:{}".format(url)
        count_key = "count:{}".format(url)

        # Check if the content is already cached
        cached_content = redis_client.get(cache_key)
        if cached_content:
            return cached_content.decode('utf-8')

        # Fetch the page content using the original function
        content = method(url)
        # Cache the content with expiration time of 10 seconds
        redis_client.setex(cache_key, 10, content)
        # Increment the access count
        redis_client.incr(count_key)

        return content
    return wrapper


@cache_page
def get_page(url: str) -> str:
    """
    Retrieve the content of a web page.

    Args:
        url (str): The URL of the web page to retrieve.

    Returns:
        str: The content of the web page as a string.
    """
    response = requests.get(url)
    return response.text
