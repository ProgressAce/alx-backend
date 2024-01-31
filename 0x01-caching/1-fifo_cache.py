#!/usr/bin/python3
"""Defines a class for caching using the FIFO strategy."""

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """A cache system using the First-In First-Out strategy."""

    # def __init__(self):
    #    super().__init__()

    def put(self, key, item):
        """Add an item to the cache storage, with regards to FIFO.

        Keys should be of similar types, eg. int, float and bool
        or only str. This is because the cache is sorted before printing
        using the builtin sorted function and thus cannot compare
        different types."""

        if not type(key) in [bool, float, int, str, tuple]:
            return

        # validate that key type can be compared with other key types
        try:
            if len(self.cache_data) > 0:
                first_key = list(self.cache_data)[0]
                comparison_possible = key > first_key
        except TypeError:
            # the key cannot be compared with other keys as it is likely
            # a different type, This is the type of the current cache type(...)
            return

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
