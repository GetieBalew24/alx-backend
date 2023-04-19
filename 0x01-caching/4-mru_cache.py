#!/usr/bin/python3
"""
a class MRUCache that inherits from BaseCaching 
and is a caching system
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Override method put() nad get()
    from BaseCaching
    """

    def __init__(self):
        """ call parent class init() methods"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Assign to the dictionary self.cache_data
        the item value for the key
        """
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS\
                    and key not in self.keys:
                deleted_key = self.keys.pop()
                del self.cache_data[deleted_key]
                print("DISCARD: {}".format(deleted_key))
            if key in self.keys:
                self.keys.remove(key)
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """return the value in self.cache_data by key.
        """
        if key in self.keys:
            self.keys.remove(key)
            self.keys.append(key)
        result = self.cache_data.get(key)
        return result