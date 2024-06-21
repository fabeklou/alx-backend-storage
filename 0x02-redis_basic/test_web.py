#!/usr/bin/env python3

from web import get_page
import redis
import time


redis_client = redis.Redis()

URL = 'http://google.com'
# URL = 'http://slowwly.robertomurray.co.uk'


# Generate cache key and count key
cache_key = "cache:{}".format(URL)
count_key = "count:{}".format(URL)

get_page(URL)
print(redis_client.get(count_key))
print(redis_client.get(cache_key))

time.sleep(12)

print(redis_client.get(count_key))
print(redis_client.get(cache_key))

for _ in range(10):
    get_page(URL)
    print(redis_client.get(count_key))
    
get_page(URL)
print(redis_client.get(count_key))
print(redis_client.get(cache_key))
