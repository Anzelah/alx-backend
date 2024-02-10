#!/usr/bin/env python3
"""create a basic caching using the lifo caching replacement technique
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Implement a LIFO caching eviction system
    """
    def __init__(self):
        """Initiliaze our instances with their initial attributes
        """
        super().__init__()
        self.list = []

    def put(self, key, item):
        """Discard items when caching is full using FIFO technique
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            newest = self.list[-1]
            print("DISCARD: {}" .format(newest))
            del self.cache_data[newest]
            del newest

        self.cache_data[key] = item
        self.list.append(key)

    def get(self, key):
        """Return a value linked to a key in dictionary
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
