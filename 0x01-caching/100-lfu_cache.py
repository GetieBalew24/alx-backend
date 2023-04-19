#!/usr/bin/env python3
"""a class LFUCache that inherits from BaseCaching 
and is a caching system:
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Override method put() nad get()
    from BaseCaching
    """
    def __init__(self):
        """call the parent class methods
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = []

    def reorder_items(self, mru_key):
        """Reorder items.
        """
        max_pos = []
        mru_frequence = 0
        mru_postion = 0
        inserted_postion = 0
        for i, key in enumerate(self.keys_freq):
            if key[0] == mru_key:
                mru_frequence = key[1] + 1
                mru_postion = i
                break
            elif len(max_pos) == 0:
                max_pos.append(i)
            elif key[1] < self.keys_freq[max_pos[-1]][1]:
                max_pos.append(i)
        max_pos.reverse()
        for pos in max_pos:
            if self.keys_freq[pos][1] > mru_frequence:
                break
            ins_pos = pos
        self.keys_freq.pop(mru_postion)
        self.keys_freq.insert(inserted_postion, [mru_key, mru_frequence])

    def put(self, key, item):
        """Adds items by using key.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                cachekey, _ = self.keys_freq[-1]
                self.cache_data.pop(cachekey)
                self.keys_freq.pop()
                print("DISCARD:", cachekey)
            self.cache_data[key] = item
            inserted_ind = len(self.keys_freq)
            for i, key_freq in enumerate(self.keys_freq):
                if key_freq[1] == 0:
                    inserted_ind = i
                    break
            self.keys_freq.insert(inserted_ind, [key, 0])
        else:
            self.cache_data[key] = item
            self.reorder_items(key)

    def get(self, key):
        """Return an item by key.
        """
        if key is not None and key in self.cache_data:
            self.reorder_items(key)
        result= self.cache_data.get(key,None)
        return result