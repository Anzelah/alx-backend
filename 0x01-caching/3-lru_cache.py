#!/usr/bin/env python3
"""The lru caching replacement technique
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """Implement a LRU caching eviction system
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Discard items using lru method when cache gets full
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru = self.cache_data.popitem(last=False)
            print("DISCARD: {}" .format(lru[0]))

    def get(self, key):
        """Return value linked to a key in the dictinary
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
