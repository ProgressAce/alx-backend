#!/usr/bin/python3
"""Defines a class for caching using the FIFO strategy."""

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """A cache system using the First-In First-Out strategy."""

    # def __init__(self):
    #    super().__init__()

    def put(self, key, item):
        """Add an item to the cache storage, with regards to FIFO."""

        if key and item:
            cache_size = len(self.cache_data)
            first_key = list(self.cache_data)[0] if cache_size > 0 else None

            key_exists = False
            if self.cache_data.get(key):
                key_exists = True

            # delete first item according to FIFO principles.
            if (cache_size == BaseCaching.MAX_ITEMS) and not key_exists:
                print(f"DISCARD:{first_key}")
                self.cache_data.pop(first_key)

            self.cache_data.update({key: item})

    def get(self, key):
        """Fetches the item, depicted by its key, from the cache storage.

        Returns:
            the item if found, otherwise "None"."""

        if self.cache_data.get(key):
            return self.cache_data.get(key)

        return None
