#!/usr/bin/python3
""" A simple BaseCaching module that will be inherited
"""


class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze instances
        Returns:
           YourCache: A new instance of the YourCache class.
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        Displays the key-value pairs in the cache, sorted by keys.
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        This method should be implemented in your specific cache class
        based on the desired caching strategy.
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        Returns:
            object or None: The item associated with the key, or None if the key is not found.
        """
        raise NotImplementedError("get must be implemented in your cache class")

