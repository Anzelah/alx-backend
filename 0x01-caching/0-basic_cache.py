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
        if key == None or item == None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve values in dictionary linked to a key
        """
        if key == None or key not in self.cache_data.keys():
            return None

        for k in self.cache_data.keys():
            if k == key:
                return self.cache_data[key]
