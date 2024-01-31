#!/usr/bin/python3
"""Defines a class for caching using the MRU strategy."""

from collections import OrderedDict

BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """A cache system using the Most Recently Used strategy."""

    def __init__(self):
        super().__init__()
        self.ordered_cache = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache storage, with regards MRU."""

        if key and item:
            cache_size = len(self.cache_data)

            # should key exist, it is popped and inserted to end for
            # reorder of recent used items
            existing_key = False
            if self.cache_data.get(key):
                self.ordered_cache.pop(key)
                existing_key = True

            # most last recently used item according to MRU principles.
            # existing keys to be updated should only result in cache reorder
            # not item deletion
            if cache_size == BaseCaching.MAX_ITEMS and (not existing_key):
                mru_key = list(self.ordered_cache)[-1]  # Most recent used key
                print(f"DISCARD:{mru_key}")
                self.cache_data.pop(mru_key)
                self.ordered_cache.pop(mru_key)

            self.cache_data.update({key: item})
            self.ordered_cache.update({key: item})  # will only be for adding

    def get(self, key):
        """Fetches the item, depicted by its key, from the cache storage.

        Returns:
            the item if found, otherwise "None"."""

        if self.cache_data.get(key):
            # reorder the recent use of items in the cache
            value = self.ordered_cache.pop(key)
            self.ordered_cache[key] = value

            return self.cache_data.get(key)

        return None
