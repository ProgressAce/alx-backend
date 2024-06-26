#!/usr/bin/env python3
""" FFIO cache system."""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ A LIFO cache system"""

    def __init__(self):
        """ Initialise a lifo cache object. It tracks order of cache items."""

        super().__init__()
        self.last_cache_key = ''

    def put(self, key, item):
        """ Adds an item to the cache while following LIFO rules.

            If the cache_size will exceed the allowed max cache size when
            adding an item, then the last added cache item will be discarded.

            Does nothing if the key or item is None."""

        if key and item:
            if len(self.cache_data) == self.MAX_ITEMS and \
                    self.cache_data.get(key) is None:
                # DISCARD last cache item
                print(f'DISCARD: {self.last_cache_key}')
                self.cache_data.pop(self.last_cache_key)

            # update last_cache_key only if the item is to be added and not updated
            # (given key is non-existent in the cache)
            if self.cache_data.get(key) is None:
                self.last_cache_key = key

            # Add item
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve the item linked to the key, in the cache.

            Returns:
                The item in the cache, or
                None if the key is None or non-existent in the cache."""

        item = self.cache_data.get(key)
        if item:
            return item

        return None
