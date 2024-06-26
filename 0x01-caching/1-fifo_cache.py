#!/usr/bin/env python3
""" FFIO cache system."""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ A FIFO cache system"""

    def __init__(self):
        """ Initialise a fifo cache object. It tracks order of cache items."""

        super().__init__()
        self.first_cache_key = ''

    def put(self, key, item):
        """ Adds an item to the cache while following FIFO rules.

            If the cache_size will exceed the allowed max cache size when
            adding an item, then the first added cache item will be discarded.

            Does nothing if the key or item is None."""

        if key and item:
            if len(self.cache_data) == self.MAX_ITEMS and \
                    self.cache_data.get(key) is None:
                # DISCARD first cache item
                print(f'DISCARD: {self.first_cache_key}')
                self.cache_data.pop(self.first_cache_key)

                # Find and set the new first cache item
                for k in self.cache_data:
                    self.first_cache_key = k
                    break

            # Add item
            self.cache_data[key] = item

            if len(self.cache_data) == 1:
                self.first_cache_key = key

    def get(self, key):
        """ Retrieve the item linked to the key, in the cache.

            Returns:
                The item in the cache, or
                None if the key is None or non-existent in the cache."""

        item = self.cache_data.get(key)
        if item:
            return item

        return None
