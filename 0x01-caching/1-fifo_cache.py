#!/usr/bin/python3
"""create a basic caching"""

from queue import Queue
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Implement a fifo caching replacement policy
    """
    def __init__(self):
        """Initiliaze our instances with their initial attributes
        Returns: Cache: A new instance of the FifoCache class.
        """
        super().__init__()
        self.list = Queue()

    def put(self, key, item):
        """Discard items when caching is full using FIFO technique
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest = self.list.get()
            del self.cache_data[oldest]
            print("DISCARD: {}" .format(oldest))

        self.cache_data[key] = item
        self.list.put(key)

    def get(self, key):
        """Return a value linked to a key in dictionary
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
