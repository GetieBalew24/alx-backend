#!/usr/bin/python3
"""
 a class LIFOCache that inherits from 
 BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Override the method put() and self()
    from basecaching class
    """

    def __init__(self):
        """ call the parent init() method"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Assign the dictionary self.cache_data 
        item value by the key
        """
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS and key not in self.stack:
                deleted_key = self.stack.pop()
                del self.cache_data[deleted_key]
                print("DISCARD: {}".format(deleted_key))
            self.cache_data[key] = item
            self.stack.append(key)

    def get(self, key):
        """Return the value in self.cache_data by key
        """
        result = self.cache_data.get(key)
        return result