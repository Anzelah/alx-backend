#!/usr/bin/env python3
"""create a basic caching using the lifo caching replacement technique
"""
from queue import LifoQueue
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Implement a caching system which uses the lifo caching replacement method
    """
    def __init__(self):
        """ Initiliaze our instances with their initial attributes
        Returns:
            LifoCache: A new instance of the LifoCache class.
        """
        super().__init__()
        self.list = LifoQueue()

    def put(self, key, item):
        """Discard items when caching is full using FIFO technique
        Returns the cache but with some items evicted and replaced
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            newest = self.list.get()
            del self.cache_data[newest]
            print("DISCARD: {}" .format(newest))

        self.cache_data[key] = item
        self.list.put(key)

    def get(self, key):
        """Return a value linked to a key in dictionary
        First check if the key is valid and if its indeed in the cache
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
