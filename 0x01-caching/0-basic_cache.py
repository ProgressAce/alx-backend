#!/usr/bin/python3
"""Defines a class for a basic caching system."""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """Represents a Basic caching system."""

    def put(self, key, item):
        """Adds a new item/data to the cache storage."""

        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Fetches an item, represented by its key, from the cache storage.

        Returns:
            the item if found, otherwise "None"."""

        if self.cache_data.get(key):
            return self.cache_data.get(key)

        return None
