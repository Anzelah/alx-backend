#!/usr/bin/python3
"""create a base caching"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Inherits from basecaching and represents a basic caching mechanism
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Assign values to our dictionary
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve values in dictionary linked to a key
        """
        if key is None or key not in self.cache_data:
            return None

        for k in self.cache_data.keys():
            if k == key:
                return self.cache_data[key]
