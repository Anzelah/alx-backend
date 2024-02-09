#!/usr/bin/python3
"""create a basic caching"""

from queue import LifoQueue
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Implement a lifo caching replacement policy
    """
    def __init__(self):
        """ Initiliaze instances
        """
        super().__init__()
        self.list = LifoQueue()

    def put(self, key, item):
        """Discard items when caching is full using FIFO technique
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
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
