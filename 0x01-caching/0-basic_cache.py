#!/usr/bin/env python3
""" Basic cache system."""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ This cache system:
      - does not have a limit
      - overloads the inherited put and get method."""

    MAX_ITEMS = -1

    def put(self, key, item):
        """ Add data to the cache.

            Does nothing should key or item be None."""

        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Returns the value of the key, in the cache.

            Returns:
                The value of the key, or
                None if key is None or doesn't exist in the cache data."""

        # will return None for non-existing key
        value = self.cache_data.get(key)
        if value:
            return value

        return None
