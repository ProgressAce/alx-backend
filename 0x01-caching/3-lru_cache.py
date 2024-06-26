#!/usr/bin/env python3
""" FFIO cache system."""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ A LRU cache system"""

    def __init__(self):
        """ Initialise a lru cache object. It tracks order of cache items."""

        super().__init__()
        # sorted from least- to most- recently used keys.
        self.recently_used_keys = []

    def put(self, key, item):
        """ Adds an item to the cache while following LRU rules.

            If the cache_size will exceed the allowed max cache size when
            adding an item then the least recently used item will be discarded.

            Does nothing if the key or item is None."""

        if key and item:
            if len(self.cache_data) == self.MAX_ITEMS and \
                    self.cache_data.get(key) is None:
                # DISCARD least recently used item
                print(f'DISCARD: {self.recently_used_keys[0]}')
                self.cache_data.pop(self.recently_used_keys[0])

                self.recently_used_keys.pop(0)

            # Add item
            self.cache_data[key] = item

            # update the most recently used key list

            # a case when an updated cache item needs their recently used
            # status updated
            idx = None
            try:
                idx = self.recently_used_keys.index(key)
            except ValueError:
                pass

            # an already existing key first needs to be removed from the list
            # to prevent duplication of the key.
            if idx is not None:
                self.recently_used_keys.pop(idx)

            # adding the key to the back indicates it is the most recently used
            self.recently_used_keys.append(key)
            print('(put) Recently used keys:', self.recently_used_keys)

    def get(self, key):
        """ Retrieve the item linked to the key, in the cache.

            Returns:
                The item in the cache, or
                None if the key is None or non-existent in the cache."""

        item = self.cache_data.get(key)
        if item:
            # update the most recently used key list
            idx = self.recently_used_keys.index(key)
            self.recently_used_keys.pop(idx)
            self.recently_used_keys.append(key)
            print('(get) Recently used keys:', self.recently_used_keys)

            return item

        return None
