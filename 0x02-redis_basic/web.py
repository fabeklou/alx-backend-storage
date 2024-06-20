#!/usr/bin/env python3

"""
This module provides functionality for caching web pages using Redis.
"""

import redis
import requests
from typing import Callable
import functools

r = redis.Redis()


def count_calls(method: Callable) -> Callable:
    """
    Decorator function that counts the number of times a method is called.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The decorated method.
    """

    @functools.wraps(method)
    def wrapper(url):
        """
        Wrapper function that increments the count for the given URL,
        checks if the HTML is cached in Redis, and retrieves it if available.
        If not cached, it calls the method to fetch the HTML,
        caches it in Redis, and returns the HTML.

        Args:
            url (str): The URL of the web page.

        Returns:
            str: The HTML content of the web page.
        """
        r.incr(f"count:{url}")
        cached_html = r.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')

        html = method(url)
        r.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_calls
def get_page(url: str) -> str:
    """
    Fetches the HTML content of a web page.

    Args:
        url (str): The URL of the web page.

    Returns:
        str: The HTML content of the web page.
    """
    req = requests.get(url)
    return req.text
