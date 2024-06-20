#!/usr/bin/env python3

"""
This module contains classes and functions for working with
Redis as a cache.

Classes:
    Cache: Represents a cache that stores data in Redis.

"""

import functools
import redis
from typing import Union, Callable, Optional
import uuid


def count_calls(method: Callable) -> Callable:
    """
    Decorator function that counts the number of times a method is called.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The decorated method.

    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator function that keeps track of the input arguments and output
    values of a method using Redis.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The decorated method.

    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = "{}:inputs".format(method.__qualname__)
        output_key = "{}:outputs".format(method.__qualname__)

        # Store input arguments
        self._redis.rpush(input_key, str(args))
        # Execute the original function
        result = method(self, *args, **kwargs)
        # Store the output
        self._redis.rpush(output_key, str(result))

        return result
    return wrapper


def replay(method: Callable) -> None:
    """
    Replays the inputs and outputs of a given method stored in Redis.

    Args:
        method (Callable): The method to replay.

    Returns:
        None

    Raises:
        None
    """
    self = method.__self__  # Access the instance of the class
    method_name = method.__qualname__
    input_key = "{}:inputs".format(method_name)
    output_key = "{}:outputs".format(method_name)

    inputs = self._redis.lrange(input_key, 0, -1)
    outputs = self._redis.lrange(output_key, 0, -1)

    print("{} was called {} times:".format(method_name, len(inputs)))
    for input_data, output_data in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(
            method_name, input_data.decode('utf-8'),
            output_data.decode('utf-8')))


class Cache:
    """
    Represents a cache that stores data in Redis.

    This class provides methods to store and retrieve data from Redis.
    It also supports optional transformation of retrieved values using
    user-defined functions.

    Attributes:
        _redis (redis.Redis): The Redis connection object.
    """

    def __init__(self):
        """
        Initializes a new instance of the Cache class.

        This function sets up the Redis connection and flushes
            the Redis database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()


class Cache:
    """
    A class that represents a cache using Redis.

    This class provides methods to store and retrieve
    data from Redis.
    It also supports optional transformation of the
    retrieved data using user-defined functions.

    Attributes:
        _redis (redis.Redis): The Redis connection object.

    Methods:
        __init__(): Initializes a new instance of the class.
    """

    def __init__(self):
        """
        Initializes a new instance of the class.

        This function sets up the Redis connection
        and flushes the Redis database.
        """

        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the given data in Redis and returns the generated key.

        Args:
            data (Union[str, bytes, int, float]): The data
                to be stored in Redis.

        Returns:
            str: The generated key used to store the data in Redis.
        """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None
            ) -> Union[int, float, str, bytes, None]:
        """
        Retrieves the value associated with the given key from Redis.

        Args:
            key (str): The key to retrieve the value for.
            fn (Optional[Callable]): An optional function to apply
                to the retrieved value.

        Returns:
            Union[int, float, str, bytes, None]: The retrieved value,
                optionally transformed by the provided function.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieves the value associated with the given key as a string.

        Args:
            key (str): The key to retrieve the value for.

        Returns:
            Optional[str]: The value associated with the key as a string,
                or None if the key does not exist.

        """
        return self.get(key, lambda data: data.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieves the value associated with the given key from the
        storage and converts it to an integer.

        Args:
            key (str): The key to retrieve the value for.

        Returns:
            Optional[int]: The value associated with the key as an integer,
            or None if the key does not exist or the value
            cannot be converted to an integer.
        """
        return self.get(key, int)
