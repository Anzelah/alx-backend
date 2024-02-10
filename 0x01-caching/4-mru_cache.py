#!/usr/bin/env python3
"""The mru caching replacement technique
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """Implement a MRU caching eviction system
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Discard items using mru method when cache gets full
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.cache_data.move_to_end(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            mru = self.cache_data.popitem()
            print("DISCARD: {}" .format(mru[0]))

    def get(self, key):
        """Return value linked to a key in the dictinary
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
