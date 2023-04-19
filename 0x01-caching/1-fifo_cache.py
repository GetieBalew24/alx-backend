#!/usr/bin/python3
"""
Task 1, a class FIFOCache that inherits 
from BaseCaching and is a caching system
"""
from base_caching import BaseCaching
from collections import deque


class FIFOCache(BaseCaching):
    """overide method  put() and get()
    """

    def __init__(self):
        """method oveloading"""
        super().__init__()
        self.queue = deque([])

    def put(self, key, item):
        """Must assign to the dictionary self.cache_data 
        the item value for the key.
        """
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS and key not in self.queue:
                deleted_key = self.queue.popleft()
                del self.cache_data[deleted_key]
                print("DISCARD: {}".format(deleted_key))
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """Return the value in self.cache_data by key
        """
        result = self.cache_data.get(key)
        return result