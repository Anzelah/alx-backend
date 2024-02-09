#!/usr/bin/python3
"""create a basic caching"""

from queue import Queue
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Implement a lifo caching replacement policy
    """
    def __init__(self):
        super().__init__()
        self.list = Queue()

    def put(self, key, item):
        """Discard item from our cache when full using the LIFO method
        """
        if key is None or itemis None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            newest = self.list.pp()
            del self.cache_data[newest]
            print("DISCARD: {}" .format(newest))

        self.cache_data[key] = item
        self.list.put(key)

    def get(self, key):
        """Return the value linked to a key in a dictionary
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data[key] = item
