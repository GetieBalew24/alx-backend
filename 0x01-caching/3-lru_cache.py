#!/usr/bin/python3
"""
 a class LRUCache that inherits from BaseCaching 
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Overide methods put() and self()
    from BaseCaching
    """
    def __init__(self):
        """call the baseCaching class init() method"""
        super().__init__()
        self.keys = []
    def put(self, key, item):
        """ Assign the dictionary self.cache_data the item value by the key
        """
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS\
                    and key not in self.keys:
                deleted_key = self.keys.pop(0)
                del self.cache_data[deleted_key]
                print("DISCARD: {}".format(deleted_key))
            if key in self.keys:
                self.keys.remove(key)
            self.cache_data[key] = item
            self.keys.append(key)
    def get(self, key):
        """Return the value an item by key
        """
        if key in self.keys:
            self.keys.remove(key)
            self.keys.append(key)
        result = self.cache_data.get(key)
        return result