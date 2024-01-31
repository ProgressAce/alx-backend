#!/usr/bin/python3
"""Defines a class for caching using the LIFO strategy."""

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """A cache system using the Last-In First-Out strategy."""

    def __init__(self):
        super().__init__()
        self.latest_key = ""

    def put(self, key, item):
        """Add an item to the cache storage, with regards to LIFO."""

        if key and item:
            cache_size = len(self.cache_data)

            key_exists = False
            if self.cache_data.get(key):
                key_exists = True

            # delete last item according to LIFO principles.
            # existing keys to be updated shouldn't result in item deletion
            if (cache_size == BaseCaching.MAX_ITEMS) and (not key_exists):
                print(f"DISCARD:{self.latest_key}")
                self.cache_data.pop(self.latest_key)

            self.cache_data.update({key: item})
            self.latest_key = key

    def get(self, key):
        """Fetches the item, depicted by its key, from the cache storage.

        Returns:
            the item if found, otherwise "None"."""

        if self.cache_data.get(key):
            return self.cache_data.get(key)

        return None
